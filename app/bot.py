import os
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

API = os.getenv("API_URL", "http://127.0.0.1:8000/chat")
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    r = requests.post(API, json={
        "text": update.message.text,
        "user_id": update.message.from_user.id
    }).json()

    await update.message.reply_text(r["response"])

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handler))
app.run_polling()
