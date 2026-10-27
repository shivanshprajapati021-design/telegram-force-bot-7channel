import os
import threading
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# --- TOKEN ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN:
    print(f"TOKEN FOUND: True - {BOT_TOKEN[:10]}...")
else:
    print("TOKEN FOUND: False - Render me BOT_TOKEN add karo")

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is Live 24/7 - 7 Channels Active"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)

# --- TUMHARE LINKS ---
CHANNELS = [
    {"name": "Channel 1", "link": "https://t.me/+j88DIVGmn2E5NzU1"},
    {"name": "Channel 2", "link": "https://t.me/+rFqJBCyqFPZlN2Q1"},
    {"name": "Channel 3", "link": "https://t.me/+cAyt8cSc44w4NjJl"},
    {"name": "Channel 4", "link": "https://t.me/+FKOANcPSQkdjMGZl"},
    {"name": "Channel 5", "link": "https://t.me/+bXf7mF-0Lh04YTY9"},
    {"name": "Channel 6", "link": "https://t.me/+vRvc1P5mRqsxZTU9"},
    {"name": "Channel 7", "link": "https://t.me/+z8wLvHX63GthN2Y1"},
]

GET_KEY_LINK = "https://t.me/+0bgzmobGphRjNjVl"
VERIFY_LINK = "https://t.me/+0bgzmobGphRjNjVl"

def make_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔴 Channel 1", url=CHANNELS[0]["link"]), InlineKeyboardButton("🔴 Channel 2", url=CHANNELS[1]["link"])],
        [InlineKeyboardButton("🔴 Channel 3", url=CHANNELS[2]["link"]), InlineKeyboardButton("🔴 Channel 4", url=CHANNELS[3]["link"])],
        [InlineKeyboardButton("🔴 Channel 5", url=CHANNELS[4]["link"]), InlineKeyboardButton("🔴 Channel 6", url=CHANNELS[5]["link"])],
        [InlineKeyboardButton("🔴 Channel 7", url=CHANNELS[6]["link"])],
        [InlineKeyboardButton("🔑 GET KEY", url=GET_KEY_LINK), InlineKeyboardButton("✅ VERIFY JOINED", callback_data="verify")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    text = f"WELCOME, {name} 👋\n\n🔥 JOIN ALL 7 CHANNELS TO UNLOCK KEY 🔥\n\nSab channel join karo fir VERIFY dabao"
    await update.message.reply_text(text, reply_markup=make_keyboard())

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    await q.message.reply_text(
        "✅ Verification Done!\n\nAb GET KEY dabao",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔑 VERIFY GET KEY", url=VERIFY_LINK)]])
    )

def main():
    threading.Thread(target=run_flask, daemon=True).start()
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(verify, pattern="verify"))
    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
