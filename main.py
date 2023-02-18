from telegram import Update ,ReplyKeyboardMarkup,keyboardbutton
from telegram.ext import CallbackContext, Updater
import requests


def start(update: Update, context: CallbackContext):
    keyboard =[
        ["dog", "cat"]
        ]
    update.message.reply_text("welcome to bot",reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))
    
def dog(update:Update,context:CallbackContext):
    response=requests.get("https://random.dog/woof.json")
    url=response.json()["url"]
    update.message.reply_photo(url)

def cat(update:Update,context:CallbackContext):
    response=requests.get("https://aws.random.cat/meow")
    url=response.json()["file"]
    update.message.reply_photo(url)
def pic(update: Update, context: CallbackContext):
    keyboard =[
        ["dog", "cat"]
        ]
    update.message.reply_text("Buttonlarning birini bosing!",reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))