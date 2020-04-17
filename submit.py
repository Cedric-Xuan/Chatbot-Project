# from __future__ import unicode_literals

import redis

# fill in the following.
# HOST = "redis-18235.c228.us-central1-1.gce.cloud.redislabs.com"
# PWD = "w2vwWBPYLIgggR0kiQzkMX7CXN4L1KjC"
# PORT = "18235"
#
# redis1 = redis.Redis(host=HOST, password=PWD, port=PORT)
#
# while True:
#     key = input("Please enter the key(type 'quit' or 'exit' to end):").strip()
#     if key == 'quit' or key == 'exit':
#         break
#     if key == '':
#         continue
#     value = input("Please enter the value (type 'quit' or 'exit' to end):").strip()
#     # Add your code here
#
#     redis1.set(key, value)
#     Y = redis1.get(key)
#     print(Y)

# from __future__ import unicode_literals

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
    RichMenuBounds, RichMenuArea, RichMenuSize, RichMenu)
from linebot.utils import PY3

import json
import requests





# _STYLE = 1
# _RESTAURANT = 2
# _FOOD = 3
# _ENVIRONMENT = 4
# _POPULAR = 5

# redis parameters
# HOST = "redis-18235.c228.us-central1-1.gce.cloud.redislabs.com"
# PWD = "w2vwWBPYLIgggR0kiQzkMX7CXN4L1KjC"
# PORT = "18235"
#
# redis1 = redis.Redis(host=HOST, password=PWD, port=PORT, decode_responses=True)

# mongodb
# client = pymongo.MongoClient("mongodb://115.220.10.112:27017/")
# db = client["admin"]  # admin - database name
# db.authenticate('myUserAdmin', 'abc123')
#
# table = client.admin
# post = table.restaurant_list
#
# app = Flask(__name__)
#
# # get channel_secret and channel_access_token from your environment variable
# channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
# channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
#
# # obtain the port that heroku assigned to this app.
# heroku_port = os.getenv('PORT', None)
#
# # if channel_secret is None:
# #     print('Specify LINE_CHANNEL_SECRET as environment variable.')
# #     sys.exit(1)
# if channel_access_token is None:
#     print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
#     sys.exit(1)

channel_access_token = 'ji9zRaSzKYpJvI7wA0WYt22Esm0nYnIVLb3DRuCNVduYsQvHuyDOPEBoHsTBdQOyBOGVgc7nKEIWrA9OiJ9jZ7WEoYf84CghITzpKy/QCTreP9lEjklPjdrOHs5Lsv21qbDxzCXIYyjmD3Tt9j8TCAdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(channel_access_token)
# parser = WebhookParser(channel_secret)


# rich_menu_to_create = RichMenu(
#     size=RichMenuSize(width=2500, height=843),
#     selected=False,
#     name="Nice richmenu",
#     chat_bar_text="Tap here",
#     areas=[RichMenuArea(
#         bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
#         action=URIAction(label='Go to line.me', uri='https://line.me'))]
# )
# rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
# print('rich_menu_id')
# print(rich_menu_id)





headers = {"Authorization":'Bearer ' + channel_access_token,"Content-Type":"application/json"}

# body = {
#     "size": {"width": 800, "height": 540},
#     "selected": "true",
#     "name": "Controller",
#     "chatBarText": "Controller",
#     "areas":[
#         {
#           "bounds": {"x": 5 , "y": 5, "width": 250, "height": 258},
#           "action": {"type": "message", "text": "Style list"}
#         },
#         {
#             "bounds": {"x": 269, "y": 5, "width": 250, "height": 258},
#             "action": {"type": "message", "text": "Call admin"}
#         },
#         {
#             "bounds": {"x": 532, "y": 5, "width": 250, "height": 258},
#             "action": {"type": "message", "text": "Style China"}
#         },
#         {
#             "bounds": {"x": 5, "y": 272, "width": 250, "height": 258},
#             "action": {"type": "message", "text": "Style Japan"}
#         },
#         {
#             "bounds": {"x": 269, "y": 272, "width": 250, "height": 258},
#             "action": {"type": "message", "text": "Style Thai"}
#         },
#         {
#             "bounds": {"x": 532, "y": 272, "width": 250, "height": 258},
#             "action": {"type": "message", "text": "Style Western"}
#         },
#     ]
#   }
# req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
#                        headers=headers, data=json.dumps(body).encode('utf-8'))


rich_menu_id = 'richmenu-b2d13d260f9910568be849decbb278aa'
#
# with open("rich_menu.png", 'rb') as f:
#     line_bot_api.set_rich_menu_image(rich_menu_id, "image/jpeg", f)



# req = requests.request('GET', 'https://api.line.me/v2/bot/richmenu/'+rich_menu_id,
#                        headers=headers)
# # #
# print('req.text')
# print(req.text)


req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+rich_menu_id,
                       headers=headers)
print('req.text')
print(req.text)


