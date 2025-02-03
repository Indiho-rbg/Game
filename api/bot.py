import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Токен бота (замінити на власний)
TOKEN = "7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU"

# Функція для обробки команди /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привіт! Я бот!")

# Ініціалізація бота
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

# Запускаємо бота у фоновому режимі
async def run_bot():
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

# Webhook для отримання оновлень від Telegram
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return JSONResponse(content={"status": "ok"})

# Встановлюємо вебхук при старті
@app.on_event("startup")
async def on_startup():
    await application.bot.set_webhook(url="https://game-three-puce.vercel.app/webhook")
    asyncio.create_task(run_bot())

# Обов'язково для Vercel
handler = app
