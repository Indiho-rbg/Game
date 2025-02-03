from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os

# Токен вашого бота
TOKEN = '7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU'

# Функція для обробки команд
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привіт! Я бот!")

# Створення та налаштування бота
application = Application.builder().token(TOKEN).build()

# Додавання обробника для команди "/start"
application.add_handler(CommandHandler("start", start))

# Створення FastAPI додатку
app = FastAPI()

# Обробка запиту від Telegram
@app.post(f'/{TOKEN}')
async def webhook(request: Request):
    json_str = await request.json()  # Виправлено на json() замість декодування вручну
    update = Update.de_json(json_str, application.bot)
    await application.process_update(update)
    return JSONResponse({"status": "ok"})

# Встановлення вебхука для бота
application.bot.set_webhook(f'https://game-three-puce.vercel.app/{TOKEN}')

# Експортуємо обробник для Vercel
handler = app
