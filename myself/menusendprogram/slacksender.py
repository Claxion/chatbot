import json
import requests
import os
import slack
from decouple import config
import datetime

# using slack 
# https://slack.dev/python-slackclient/basic_usage.html#sending-a-message

#오늘의 식사 시간 
#오늘의 메뉴 A, B 
#메뉴가 하나일 경우에는 하나만
# content에 입력
# 0 : 월 1 : 화 2 : 수 3 : 목 4 : 금 

def sendMenuByDay(theDay):
    pass


def slackrun() :
    # Bot User OAuth Access Token 을 사용한다.
    slack_token = config("TESTMENUSLACKTOKEN") # test
    #slack_token = config("SSAFYMENUSLACKTOKEN") # ssafy
    
    client = slack.WebClient(token = slack_token)
    #client.chat_postMessage(
    #channel="general",
    #text="Hello from your app! :tada:"
#)
#     client.chat_postMessage(
#   channel="menu",
#   blocks=[
#     {
#         "type": "section",
#         "text": {
#             "type": "mrkdwn",
#             "text": "Danny Torrence left the following review for your property:"
#         }
#     },
#     {
#         "type": "section",
#         "text": {
#             "type": "mrkdwn",
#             "text": "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room " +
#             "237 was far too rowdy, whole place felt stuck in the 1920s."
#         },
#         "accessory": {
#             "type": "image",
#             "image_url": "https://images.pexels.com/photos/750319/pexels-photo-750319.jpeg",
#             "alt_text": "Haunted hotel image"
#         }
#     },
#     {
#         "type": "section",
#         "fields": [
#             {
#                 "type": "mrkdwn",
#                 "text": "*Average Rating*\n1.0"
#             }
#         ]
#     }
#   ]
# )
    client.files_upload(
    channels="menu",
    file=r"C:\Users\student\Downloads\menu.png",
    title="Test upload"
)

if __name__ == '__main__' :
    #slackrun()