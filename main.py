import os, threading, time
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
print(f"TOKEN CHECK: {BOT_TOKEN[:15] if BOT_TOKEN else 'NOT FOUND'}")

app_flask = Flask(__name__)
@app_flask.route('/')
def home(): return "Bot is Live - Add BOT_TOKEN in Env"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)

CHANNELS = [
    "https://t.me/+j88DIVGmn2E5NzU1",
    "https://t.me/+rFqJBCyqFPZlN2Q1",
    "https://t.me/+cAyt8cSc44w4NjJl",
    "https://t.me/+FKOANcPSQkdjMGZl",
    "https://t.me/+bXf7mF-0Lh04YTY9",
    "https://t.me/+vRvc1P5mRqsxZTU9",
    "https://t.me/+z8wLvHX63GthN2Y1",
]
GET_KEY = "https://t.me/+0bgzmobGphRjNjVl"

def make_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel 1", url=CHANNELS[0]), InlineKeyboardButton("Channel 2", url=CHANNELS[1])],
        [InlineKeyboardButton("Channel 3", url=CHANNELS[2]), InlineKeyboardButton("Channel 4", url=CHANNELS[3])],
        [InlineKeyboardButton("Channel 5", url=CHANNELS[4]), InlineKeyboardButton("Channel 6", url=CHANNELS[5])],
        [InlineKeyboardButton("Channel 7", url=CHANNELS[6])],
        [InlineKeyboardButton("🔑 GET KEY", url=GET_KEY), InlineKeyboardButton("✅ VERIFY", callback_data="verify")]
    ])

async def start(update, context):
    await update.message.reply_text(f"WELCOME {update.effective_user.first_name}\nJoin all 7 to get key", reply_markup=make_keyboard())

async def verify(update, context):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text("Verified!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("GET KEY", url=GET_KEY)]]))

def main():
    threading.Thread(target=run_flask, daemon=True).start()
    if not BOT_TOKEN:
        print("No BOT_TOKEN - only Flask running")
        while True: time.sleep(3600)
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(verify, pattern="verify"))
    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__": main()
