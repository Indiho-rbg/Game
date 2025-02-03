import logging
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Логування
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Токен бота
TOKEN = "7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU"

# Функція для обробки команди /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привіт! Я бот!")

# Ініціалізація бота
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

# Webhook для отримання оновлень від Telegram
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return JSONResponse(content={"status": "ok"})

# Встановлення вебхука при старті
@app.on_event("startup")
async def on_startup():
    await application.bot.set_webhook(url="https://game-three-puce.vercel.app/webhook")
    asyncio.create_task(application.run_polling())

# Обов'язково для Vercel
handler = app
