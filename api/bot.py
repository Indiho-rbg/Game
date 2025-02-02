import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

# Ініціалізація FastAPI
app = FastAPI()

# Додаємо кореневий маршрут для перевірки роботи сервера
@app.get("/")
async def root():
    return {"message": "Бот працює! Вебхук налаштовано."}
    
# Токен вашого бота (замініть на свій)
TOKEN = '7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU'

# Функція для обробки команд
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привіт! Я бот!")

# Створення та налаштування бота
application = Application.builder().token(TOKEN).build()

# Обробка запиту від Telegram
@app.post(f'/{TOKEN}')
async def webhook(request: Request):
    json_str = await request.json()  # Виправлено на json() замість декодування вручну
    update = Update.de_json(json_str, application.bot)
    await application.process_update(update)  # Використовуємо process_update замість dispatcher.process_update
    return JSONResponse({"status": "ok"})

# Встановлення вебхука для бота
application.bot.set_webhook(f'https://game-three-puce.vercel.app/{TOKEN}')

# Запуск сервера (лише для локального запуску, на Vercel не потрібен)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
