from flask import Flask, request

echo_app = Flask(__name__)

@echo_app.route('/')
def main():
    return 'ok'


if __name__ == '__main__':
    echo_app.run()