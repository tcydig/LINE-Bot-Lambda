import os
import sys
import logging
import json
import urllib.request
from linebot import LineBotApi
from linebot.models import TextSendMessage

# Log
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

# lambda環境変数より取得（Lineチャネルアクセストークン・LineユーザID）
channel_access_token = os.environ['CHANNEL_ACCESS_TOKEN']
user_id = os.environ['USER_ID']

# 環境変数より値が取得出来ない場合はエラー
if user_id is None:
    logger.error('Specify user_id as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    logger.error('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)
line_bot_api = LineBotApi(channel_access_token)

def lambda_handler(event, context):

    messages = TextSendMessage(text="本文")
    line_bot_api.push_message(
            user_id,
            messages=messages)

    return {
        'statusCode': 200,
        'body': json.dumps('Thanks for Lambda!')
    }
