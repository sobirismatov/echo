from flask import Flask, request
from telegram import Bot
import os
echo_app = Flask(__name__)

TOKEN=os.environ(token=TOKEN)
bot=Bot(TOKEN)

@echo_app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        print("dsgd")
        return 'hi from Husniddin'
        
    elif request.method == 'POST':
        data = request.get_json(force=True)
        chat_id=data["message"]["from"]["id"]
        text=data["message"]["text"]
        print(chat_id, text)
        bot.send_message(chat_id,text)

        return 'hello'
if __name__=="__main__":
    echo_app.run()
