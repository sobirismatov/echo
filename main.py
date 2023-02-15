from flask import Flask, request

echo_app = Flask(__name__)

@echo_app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        print("dsgd")
        return 'hi from Husniddin'
        
    elif request.method == 'POST':
        data = request.get_json(force=True)
        print(data)
        # chat_id=data["massage"]["from"]["id"]
        # text=data["massage"]["text"]
        # print(chat_id, text)

        return 'hello'