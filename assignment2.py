from __future__ import unicode_literals

import os
import sys
import redis

from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, VideoMessage, FileMessage, StickerMessage,
    StickerSendMessage
)
from linebot.utils import PY3

import json

_STYLE = 1
_RESTAURANT = 2
_FOOD = 3
_ENVIRONMENT = 4

# redis parameters
HOST = "redis-18235.c228.us-central1-1.gce.cloud.redislabs.com"
PWD = "w2vwWBPYLIgggR0kiQzkMX7CXN4L1KjC"
PORT = "18235"

redis1 = redis.Redis(host=HOST, password=PWD, port=PORT, decode_responses=True)

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

    if label == _STYLE:
        msg = 'Sorry, Not Found.'
        query = 'style_restaurant_list'
        style_name = extract_style_data(text)
        result_json_str = redis1.get(query)

        if (result_json_str is not None) and (style_name in result_json_str):
            result_json = json.loads(result_json_str)

            result = 'Style:' + style_name + '\n'

            if result_json[style_name] is not None:
                if len(result_json[style_name]) > 0:

                    for restaurant in result_json[style_name]:
                        result += restaurant['restaurant'] + '\tTel:' + restaurant['tel'] + '\n' + 'Address:' + restaurant[
                            'address'] + '\n'

                    msg = result


    elif label == _RESTAURANT:
        msg = 'Sorry, Not Found.'
        query = 'restaurant_' + extract_restaurant_data(text)
        result_json_str = redis1.get(query)

        if result_json_str is not None:
            result_json = json.loads(result_json_str)

            popular_list = result_json['popular_menu']

            if len(popular_list) > 0:

                result = 'Restaurant:' + result_json['restaurant'] + '\n' + 'Popular Dishes:\n'

                for dish in popular_list:
                    result += '\t' + dish['dish'] + '\t $' + str(dish['price']) + '\n'

                msg = result

    elif label == _FOOD:
        msg = 'Sorry, Not Found.'
        img_url = ''
        dish_name = ''
        restaurant, food = extract_restaurant_food_data(text)
        query = 'restaurant_' + restaurant
        print('query:' + query)
        json_string = redis1.get(query)
        if json_string is not None:
            json_object = json.loads(json_string)
            popular_menu_list = json_object['popular_menu']
            if len(popular_menu_list) > 0:
                for dish in popular_menu_list:
                    if dish['dish'] == food:
                        print('Found dish:' + dish['dish'])
                        img_url = dish['img_url']
                        dish_name = dish['dish']
                        break

        if dish_name != '' and img_url != '':
            msg = 'Restaurant:' + restaurant + '\n' + 'Dish:' + dish_name + '\n' + img_url

    elif label == _ENVIRONMENT:
        msg = 'Sorry, Not Found.'
        img_url = ''
        restaurant = extract_restaurant_environment(text)
        query = 'restaurant_' + restaurant
        print('query:' + query)
        json_string = redis1.get(query)
        if json_string is not None:
            json_object = json.loads(json_string)
            img_url = json_object['environment']

            if img_url != '':
                msg = 'Restaurant:' + restaurant + '\n' + 'Environment Picture:' + img_url

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(msg)
    )


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


def classify_TextMessage(text):
    text = str(text)
    if 'style' in text:
        return _STYLE
    elif ('food' in text) and ('restaurant' in text):
        return _FOOD
    elif 'restaurant' in text and 'environment' not in text:
        return _RESTAURANT
    elif ('environment' in text) and ('restaurant' in text):
        return _ENVIRONMENT


def extract_style_data(text):
    key = 'style'
    return text[text.index(key) + 5:].strip()


def extract_restaurant_data(text):
    key = 'restaurant'
    return text[text.index(key) + 10:].strip()


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


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(host='0.0.0.0', debug=options.debug, port=heroku_port)
