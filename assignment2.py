from __future__ import unicode_literals

import os
import sys
from datetime import datetime

import redis
import pymongo

from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError,
    LineBotApiError)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, VideoMessage, FileMessage, StickerMessage,
    StickerSendMessage,
    ImageSendMessage, LocationSendMessage, VideoSendMessage, QuickReply, TemplateSendMessage,
    PostbackAction, MessageAction, URIAction, ButtonsTemplate, URIImagemapAction, LocationAction, QuickReplyButton,
    RichMenuBounds, RichMenuArea, RichMenuSize, RichMenu, CarouselTemplate, CarouselColumn, ConfirmTemplate)
from linebot.utils import PY3

import json as Json
import requests
import random

_ALL_STYLE = 0
_STYLE = 1
_STYLE_IN_LIST = 2
_RESTAURANT = 3
_FOOD = 4
_ENVIRONMENT = 5
_POPULAR = 6
_LOCATION = 7
_CALL_US = 8
_NEARBY = 9

#Google map API key
GOOGLE_API_KEY = ''  # due to confidentiality, it will not be published on GitHub

# redis parameters
HOST = "redis-18235.c228.us-central1-1.gce.cloud.redislabs.com"
PWD = "w2vwWBPYLIgggR0kiQzkMX7CXN4L1KjC"
PORT = "18235"

redis1 = redis.Redis(host=HOST, password=PWD, port=PORT, decode_responses=True)

# mongodb
client = pymongo.MongoClient("mongodb://115.220.10.112:27017/")
db = client["admin"]  # admin - database name
db.authenticate('myUserAdmin', 'abc123')

table = client.admin
post = table.restaurant_list

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

# obtain the port that heroku assigned to this app.
heroku_port = os.getenv('PORT', None)

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        print('event: ' + str(event))

        # if (event.type == 'postback'):
        #     handle_Postback_Message(event)

        if not isinstance(event, MessageEvent):
            continue
        if isinstance(event.message, TextMessage):
            handle_TextMessage(event)
        if isinstance(event.message, ImageMessage):
            handle_ImageMessage(event)
        if isinstance(event.message, VideoMessage):
            handle_VideoMessage(event)
        if isinstance(event.message, FileMessage):
            handle_FileMessage(event)
        if isinstance(event.message, StickerMessage):
            handle_StickerMessage(event)

        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

    return 'OK'


# Handler function for Text Message
def handle_TextMessage(event):
    # print(event.message.text)

    text = event.message.text.lower()
    print(text)

    label = classify_TextMessage(text)

    if label == _ALL_STYLE:

        style_list = []
        for style in post.distinct('style'):
            style_list.append(post.find_one({'style': style}, {'style': 1, 'popular_menu': {"$slice": 1}, '_id': 0}))

        send_all_style_list_button_message(event, style_list)

        user = Json.loads(str(event.source))
        uid = user['userId']
        redis1.incr(text)
        redis1.incr(text + '-' + uid)

    elif label == _STYLE:
        msg = 'Sorry, Not Found.'
        style_name = extract_style_data(text)
        query = {'style': style_name}
        print('query:' + str(query))
        result_json = post.find(query)

        if result_json is not None:
            # result_json = json.loads(result_json_str)

            # result = 'Style:' + style_name + '\n\n'

            # for restaurant in result_json:
            #     result += restaurant['restaurant'] + '\tTel:' + restaurant['tel'] + '\n' + 'Address:' + restaurant[
            #         'address'] + '\n\n'

            send_restaurant_list_button_message(event, style_name, result_json)

            user = Json.loads(str(event.source))
            uid = user['userId']
            redis1.incr(text)
            redis1.incr(text + '-' + uid)




    elif label == _STYLE_IN_LIST:
        msg = 'Sorry, Not Found.'
        style_name = extract_style_in_list_data(text)
        query = {'style': style_name}
        print('query:' + str(query))
        result_json = post.find(query)

        if result_json is not None:
            # result_json = json.loads(result_json_str)

            result = 'Style:' + style_name + '\n\n'

            for restaurant in result_json:
                result += restaurant['restaurant'] + '\tTel:' + restaurant['tel'] + '\n' + 'Address:' + restaurant[
                    'address'] + '\n\n'

            msg = result

            user = Json.loads(str(event.source))
            uid = user['userId']
            redis1.incr(text)
            redis1.incr(text + '-' + uid)

        send_text_message(event, msg)


    elif label == _RESTAURANT:
        msg = 'Sorry, Not Found.'
        address = ''
        latitude = ''
        longitude = ''
        title = ''
        query = {'restaurant': extract_restaurant_data(text)}
        print('query:' + str(query))
        result_json = post.find_one(query)

        if result_json is not None:

            title = result_json['restaurant']
            if ('address' in result_json) and ('latitude' in result_json) and ('longitude' in result_json):
                address = result_json['address']
                latitude = result_json['latitude']
                longitude = result_json['longitude']

            popular_list = result_json['popular_menu']

            if len(popular_list) > 0:
                # result = 'Restaurant:' + result_json['restaurant'] + '\n\n' + 'Tel:' + result_json[
                #     'tel'] + '\nAddress:' + result_json['address'] + '\nPopular Dishes:\n'
                #
                # for dish in popular_list:
                #     result += '\t' + dish['dish'] + '\t $' + str(dish['price']) + '\n'
                #
                # msg = result
                send_restaurant_button_message(event, result_json['environment'], title, address, result_json['tel'])

            user = Json.loads(str(event.source))
            uid = user['userId']
            redis1.incr(text)
            redis1.incr(text + '-' + uid)

        # send_text_message(event, msg)
        # if title != '' and address != '' and latitude != '' and longitude != '':
        #
        #     send_location_message(event, title, address, latitude, longitude)

    elif label == _POPULAR:
        title = ''
        query = {'restaurant': extract_popular_dishes_data(text)}
        print('query:' + str(query))
        result_json = post.find_one(query)
        if result_json is not None:

            popular_list = result_json['popular_menu']

            if len(popular_list) > 0:

                result = 'Restaurant:' + result_json['restaurant'] + '\nPopular Dishes:\n'

                for dish in popular_list:
                    result += '\t' + dish['dish'] + '\t $' + str(dish['price']) + '\n'

                all_text = result

            send_popular_dishes_button_message(event, result_json['restaurant'], result_json['popular_menu'], all_text)

            user = Json.loads(str(event.source))
            uid = user['userId']
            redis1.incr(text)
            redis1.incr(text + '-' + uid)

    elif label == _FOOD:
        msg = 'Sorry, Not Found.'
        img_url = ''
        dish_name = ''
        price = ''
        restaurant, food = extract_restaurant_food_data(text)
        query = {'restaurant': restaurant}
        print('query:' + str(query))
        json = post.find_one(query)
        if json is not None:

            popular_menu_list = json['popular_menu']
            if len(popular_menu_list) > 0:
                for dish in popular_menu_list:
                    if dish['dish'] == food:
                        print('Found dish:' + dish['dish'])
                        img_url = dish['img_url']
                        dish_name = dish['dish']
                        price = str(dish['price'])
                        break

        if dish_name != '' and img_url != '':
            msg = 'Restaurant:' + restaurant + '\n' + 'Dish:' + dish_name + '\tPrice: $' + price
            send_text_message(event, msg)
            send_image_message(event, img_url, img_url)
        elif dish_name != '' and img_url == '':
            msg = 'Restaurant:' + restaurant + '\n' + 'Dish:' + dish_name + '\tPrice: $' + price + '\nSorry, there no image about the dish.'
            send_text_message(event, msg)
        else:
            send_text_message(event, msg)

        if json is not None:
            user = Json.loads(str(event.source))
            uid = user['userId']
            redis1.incr(text)
            redis1.incr(text + '-' + uid)

    elif label == _ENVIRONMENT:
        msg = 'Sorry, Not Found.'
        img_url = ''
        video_url = ''
        video_img = ''
        restaurant = extract_restaurant_environment(text)
        query = {'restaurant': restaurant}
        print('query:' + str(query))
        json = post.find_one(query)
        if json is not None:

            if 'environment' in json:
                img_url = json['environment']

            if ('video' in json) and ('video_img' in json):
                video_img = json['video_img']
                video_url = json['video']

        if img_url != '':
            msg = 'Restaurant:' + restaurant
            send_text_message(event, msg)
            send_image_message(event, img_url, img_url)

        else:
            msg = 'Restaurant:' + restaurant + '\nSorry, here no image about the restaurant.'
            send_text_message(event, msg)

        if video_url != '' and video_img != '':
            send_video_message(event, video_img, video_url)

        if (img_url == '') and (video_url == '') and (video_img == ''):
            send_text_message(event, 'Sorry, Not Found.')

        if json is not None:
            user = Json.loads(str(event.source))
            uid = user['userId']
            redis1.incr(text)
            redis1.incr(text + '-' + uid)

    elif label == _LOCATION:

        restaurant = extract_location_data(text)
        query = {'restaurant': restaurant}
        print('query:' + str(query))
        json = post.find_one(query)

        if json is not None:

            title = json['restaurant']
            if ('address' in json) and ('latitude' in json) and ('longitude' in json):
                address = json['address']
                latitude = json['latitude']
                longitude = json['longitude']

            if title != '' and address != '' and latitude != '' and longitude != '':
                send_location_message(event, title, address, latitude, longitude)

            user = Json.loads(str(event.source))
            uid = user['userId']
            redis1.incr(text)
            redis1.incr(text + '-' + uid)


    elif label == _CALL_US:
        send_call_us_button_message(event)

    elif label == _NEARBY:
        nearby = extract_nearby_data(text)
        restaurant_list, image_list, map_url_lit = get_3_restaurants_nearby(nearby)
        send_nearby_restaurant_list_message(event, restaurant_list, image_list, map_url_lit)

        user = Json.loads(str(event.source))
        uid = user['userId']
        redis1.incr('nearby')
        redis1.incr('nearby-' + uid)

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(msg)
    # )


# Handler function for Sticker Message
def handle_StickerMessage(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )


# Handler function for Image Message
def handle_ImageMessage(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Nice image!")
    )


# Handler function for Video Message
def handle_VideoMessage(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Nice video!")
    )


# Handler function for File Message
def handle_FileMessage(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Nice file!")
    )


# def handle_Postback_Message(event):
#
#     js = json.loads(event.postback.data)
#     if js['type'] == 'location':
#         print('2com')
#         send_location_message(event, js['title'],js['address'], js['latitude'], js['longitude'])


def classify_TextMessage(text):
    text = str(text)
    if ('style list of' in text):
        return _STYLE_IN_LIST
    elif ('style list' in text):
        return _ALL_STYLE
    elif ('style' in text) and ('list' not in text):
        return _STYLE
    elif ('food' in text) and ('restaurant' in text):
        return _FOOD
    elif 'restaurant' in text and 'environment' not in text:
        return _RESTAURANT
    elif ('environment' in text) and ('restaurant' in text):
        return _ENVIRONMENT
    elif ('popular' in text) and ('dishes' in text):
        return _POPULAR
    elif 'location' in text:
        return _LOCATION
    elif 'call admin' in text:
        return _CALL_US
    elif 'nearby' in text:
        return _NEARBY


def extract_style_data(text):
    key = 'style'
    return text[text.index(key) + 5:].strip()


def extract_style_in_list_data(text):
    key = 'style list of'
    print('extract:', text)
    return text[text.index(key) + 13:].strip()


def extract_restaurant_data(text):
    key = 'restaurant'
    return text[text.index(key) + 10:].strip()


def extract_popular_dishes_data(text):
    key = 'popular dishes'
    return text[text.index(key) + 14:].strip()


def extract_restaurant_food_data(text):
    key1 = 'restaurant'
    key2 = 'food'

    result1 = text[text.index(key1) + 10:]
    result_list = result1.split(key2)
    result1 = result_list[0].strip()
    result2 = result_list[1].strip()

    return result1, result2


def extract_restaurant_environment(text):
    key1 = 'restaurant'
    key2 = 'environment'

    result1 = text[text.index(key1) + 10:]
    result_list = result1.split(key2)
    result1 = result_list[0].strip()

    return result1


def extract_location_data(text):
    key = 'location'
    return text[text.index(key) + 8:].strip()


def extract_nearby_data(text):
    key = 'nearby'
    return text[text.index(key) + 6:].strip()


def get_3_restaurants_nearby(nearby):
    restaurant_list = []
    thumbnail_image_url_list = []
    map_url_list = []

    addurl = 'https://maps.googleapis.com/maps/api/geocode/json?key={}&address={}&sensor=false'.format(GOOGLE_API_KEY,
                                                                                                       nearby)

    # get current location
    addressReq = requests.get(addurl)
    addressDoc = addressReq.json()
    if len(addressDoc['results']) <= 0:
        return restaurant_list, thumbnail_image_url_list, map_url_list
    lat = addressDoc['results'][0]['geometry']['location']['lat']
    lng = addressDoc['results'][0]['geometry']['location']['lng']

    # get pharmacies around this location
    restaurantSearch = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={}&location={},{}&rankby=distance&type=restaurant&language=en-US'.format(
        GOOGLE_API_KEY, lat, lng)
    restaurantReq = requests.get(restaurantSearch)
    nearby_restaurant_dict = restaurantReq.json()

    # put the searching result into top20_restaurant as a list
    top20_restaurant = nearby_restaurant_dict['results']
    res_num = (len(top20_restaurant))

    # get the restaurant whose rating is beyond 4
    bravo = []
    for i in range(res_num):
        try:
            if top20_restaurant[i]['rating'] > 4:
                print('rating', top20_restaurant[i]['rating'])
                bravo.append(i)
        except:
            KeyError
    # if all restaurants' rating are lower than 4, randomly choose three

    if len(bravo) < 3:
        content = 'there is no restaurant around'
        restaurant_list = (random.sample(top20_restaurant, 3))
        # or choose from bravo list
    else:
        index_list = random.sample(bravo, 3)
        for index in index_list:
            restaurant_list.append(top20_restaurant[index])

        # check the photo of this restaurant

    for i in range(len(restaurant_list)):
        if restaurant_list[i].get('photos') is None:
            thumbnail_image_url_list.append(
                'https://lh3.googleusercontent.com/proxy/picnJy4RcLmy7gLgcbPscFTw8HHcou5wiPFk-dxHTH8-XNse7PEH2nNrUQXkzMbSPeFhdfi2j5G3uGILpJPTqriYuS2cyPDjWGUST9zLwTbrlrswoBxwuGe8AaVZx7JV-vBoZsque3I5')
        else:
            # if has photos, choose 3
            photo_reference = restaurant_list[i]['photos'][0]['photo_reference']
            photo_width = restaurant_list[i]['photos'][0]['width']
            thumbnail_image_url_list.append(
                'https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}'.format(
                    GOOGLE_API_KEY, photo_reference, photo_width))

        restaurant_list[i]['rating'] = 'no rating' if restaurant_list[i].get('rating') is None else restaurant_list[i][
            'rating']
        restaurant_list[i]['vicinity'] = 'No info' if restaurant_list[i].get('vicinity') is None else \
        restaurant_list[i]['vicinity']

        # the url of current map
        lat = str(restaurant_list[i]['geometry']['location']['lat'])
        long = str(restaurant_list[i]["geometry"]['location']['lng'])
        place_id = str(restaurant_list[i]['place_id'])

        map_url_list.append(
            "http://www.google.com/maps/search/?api=1&query=" + lat + "," + long + "&query_place_id=" + place_id)

    return restaurant_list, thumbnail_image_url_list, map_url_list


def send_text_message(event, msg_text):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(msg_text)
    )


def send_image_message(event, msg_img_url, msg_preview_img_url):
    print('img:', type(msg_img_url))
    print('pre_img:', msg_img_url)
    print('user', event.source)
    print('reply_token', event.reply_token)

    user = Json.loads(str(event.source))
    print(user['userId'])

    try:
        line_bot_api.push_message(
            user['userId'],
            ImageSendMessage(original_content_url=msg_img_url, preview_image_url=msg_preview_img_url)
        )
    except LineBotApiError as e:
        raise e


def send_location_message(event, msg_title, msg_address, msg_latitude, msg_longitude):
    print('latitude', msg_latitude)
    print('longitude', msg_longitude)

    user = Json.loads(str(event.source))
    print(user['userId'])

    try:
        line_bot_api.push_message(
            user['userId'],
            LocationSendMessage(title=msg_title, address=msg_address, latitude=msg_latitude, longitude=msg_longitude)
        )
    except LineBotApiError as e:
        raise e


def send_video_message(event, msg_video_img_url, msg_video_url):
    print('video_img_url', msg_video_img_url)
    print('video_url', msg_video_url)

    user = Json.loads(str(event.source))
    print(user['userId'])

    try:
        line_bot_api.push_message(
            user['userId'],
            VideoSendMessage(original_content_url=msg_video_url, preview_image_url=msg_video_img_url)
        )
    except LineBotApiError as e:
        raise e


def send_all_style_list_button_message(event, style_list):
    user = Json.loads(str(event.source))
    uid = user['userId']
    print('userId')
    print(uid)

    message = TemplateSendMessage(

        alt_text='Style List',
        template=CarouselTemplate(
            columns=[CarouselColumn(thumbnail_image_url=style['popular_menu'][0]['img_url'], title=style['style'],
                                    text=style['style'],
                                    actions=[MessageAction(label=style['style'], text='style ' + style['style'])]) for
                     style in style_list]
        ))

    try:
        line_bot_api.push_message(
            uid,
            message
        )
    except LineBotApiError as e:
        raise e


def send_restaurant_button_message(event, image_url, title, address, tel):
    user = Json.loads(str(event.source))
    uid = user['userId']
    print('userId')
    print(uid)
    message = TemplateSendMessage(
        alt_text='Restaurant Buttons',
        template=ButtonsTemplate(
            thumbnail_image_url=image_url,
            title=title,
            text='Address:' + address,
            actions=[
                PostbackAction(
                    label='Popular dishes',
                    text='Popular dishes ' + title,
                    data='action=1'
                ),
                PostbackAction(
                    label='Environment',
                    text='restaurant ' + title + ' environment',
                    data='action=Environment'
                ),
                PostbackAction(
                    label='Location',
                    data='action=location',
                    text='location ' + title
                ),
                URIAction(
                    label='CALL',
                    uri='tel:' + str(tel)
                ),

            ]
        )
    )
    try:
        line_bot_api.push_message(
            uid,
            message
        )
    except LineBotApiError as e:
        raise e


def send_popular_dishes_button_message(event, restaurant, dishes, all_text):
    user = Json.loads(str(event.source))
    uid = user['userId']
    print('userId')
    print(uid)
    items = [QuickReplyButton(action=MessageAction(label=dish['dish'] + ' $' + str(dish['price']),
                                                   text='restaurant ' + restaurant + ' food ' + dish['dish'])) for dish
             in dishes]
    items.insert(0, QuickReplyButton(action=MessageAction(label='All list', text=all_text)))
    message = TextSendMessage(text='Popular dishes', quick_reply=QuickReply(items=items))
    try:
        line_bot_api.push_message(
            uid,
            message
        )
    except LineBotApiError as e:
        raise e


def send_restaurant_list_button_message(event, title, restaurant_list):
    user = Json.loads(str(event.source))
    uid = user['userId']
    print('userId')
    print(uid)

    items = [
        PostbackAction(label=restaurant['restaurant'], text='restaurant ' + restaurant['restaurant'], data='action=1')
        for restaurant in restaurant_list]
    items.insert(0, PostbackAction(label='All in list', text='style list of ' + title, data='action=1'))

    message = TemplateSendMessage(
        alt_text='Restaurant Buttons',
        template=ButtonsTemplate(
            thumbnail_image_url=None,
            title=title,
            text='Restaurant List',
            actions=items
        )
    )
    try:
        line_bot_api.push_message(
            uid,
            message
        )
    except LineBotApiError as e:
        raise e


def send_call_us_button_message(event):
    user = Json.loads(str(event.source))
    uid = user['userId']
    print('userId')
    print(uid)

    message = TemplateSendMessage(
        alt_text='Confirm to call us',
        template=ConfirmTemplate(
            text='Confirm to call us?',
            actions=[
                URIAction(
                    label='Yes',
                    text='Yes',
                    uri='tel:85263329050'
                ),
                MessageAction(
                    label='No',
                    text='Cancel to call',
                    # data='action=cancel_call'
                )
            ]
        )
    )

    try:
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    except LineBotApiError as e:
        raise e


def send_nearby_restaurant_list_message(event, restaurant_list, image_list, map_url_list):
    user = Json.loads(str(event.source))
    uid = user['userId']
    print('userId')
    print(uid)

    if len(restaurant_list) <= 0:
        send_text_message(event, 'Sorry, not found.')
        return

    items = []

    for i in range(len(restaurant_list)):
        title = restaurant_list[i]['name'][:37] + '...' if len(restaurant_list[i]['name']) > 39 else restaurant_list[i][
            'name']
        vicinity = restaurant_list[i]['vicinity'][:27] + '...' if len(restaurant_list[i]['vicinity']) > 30 else \
        restaurant_list[i]['vicinity']
        print(title)
        print(vicinity)
        items.append(

            CarouselColumn(thumbnail_image_url=image_list[i], title=title,
                           text='Rating:' + str(restaurant_list[i]['rating']) + '\nAddress:' + vicinity,
                           actions=[URIAction(label='Navigation', uri=map_url_list[i])])
        )

    message = TemplateSendMessage(

        alt_text='Recommend List',
        template=CarouselTemplate(
            columns=items
        ))

    try:
        line_bot_api.push_message(
            uid,
            message
        )
    except LineBotApiError as e:
        raise e


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(host='0.0.0.0', debug=False, port=heroku_port, threaded=True)
