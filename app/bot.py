import os
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

API = os.getenv("API_URL")
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = requests.post(
            API,
            json={
                "text": update.message.text,
                "user_id": update.message.from_user.id,
            },
            timeout=10,
        )

        print("STATUS:", r.status_code)
        print("BODY:", r.text)

        data = r.json()

        await update.message.reply_text(
            data.get("response", f"Ошибка API:\n{data}")
        )

    except Exception as e:
        await update.message.reply_text(f"Ошибка:\n{e}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handler))
app.run_polling()
