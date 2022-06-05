from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('+g3stbkcgW0GH3Xtu+vUpfbwq8UqVk5wwZrnsclD8brse9OCFq3P4GEjsoIYFIC3BxAI+J74RH62H34tndlvI3dTkj492WY4MuDY3gg98ohTmd9ZyVTqLz3PUtOhso5XXmblUNdeP4Xw3G36VuXEuAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('37d30c7987a038f0a9b2217912092b59')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()