import os
import threading
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "BOT LIVE - 7 CHANNEL FORCE BOT"

def run_bot():
    # Agar token nahi hai to bot start nahi hoga
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN not found in Render Environment Variables")
        return
    
    C1 = "https://t.me/+j88DIVGmn2E5NzU1"
    C2 = "https://t.me/+rFqJBCyqFPZlN2Q1"
    C3 = "https://t.me/+cAyt8cSc44w4NjJl"
    C4 = "https://t.me/+FKOANcPSQkdjMGZl"
    C5 = "https://t.me/+bXf7mF-0Lh04YTY9"
    C6 = "https://t.me/+vRvc1P5mRqsxZTU9"
    C7 = "https://t.me/+z8wLvHX63GthN2Y1"
    GET_KEY = "https://t.me/+0bgzmobGphRjNjVl"
    VERIFY = "https://t.me/+0bgzmobGphRjNjVl"

    def keyboard():
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("SLOT 1", url=C1), InlineKeyboardButton("SLOT 2", url=C2)],
            [InlineKeyboardButton("SLOT 3", url=C3), InlineKeyboardButton("SLOT 4", url=C4)],
            [InlineKeyboardButton("SLOT 5", url=C5), InlineKeyboardButton("SLOT 6", url=C6)],
            [InlineKeyboardButton("SLOT 7", url=C7)],
            [InlineKeyboardButton("GET KEY", url=GET_KEY)],
            [InlineKeyboardButton("VERIFY", callback_data="verify")]
        ])

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = "WELCOME\n\nJoin all 7 channels to get key\n\nGET KEY link: " + GET_KEY
        await update.message.reply_text(msg, reply_markup=keyboard())

    async def verify_cb(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.callback_query.answer()
        await update.callback_query.message.reply_text(
