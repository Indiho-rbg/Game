from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, CallbackContext
import os

# 1. Створення об'єкта FastAPI
app = FastAPI()

# Токен вашого Telegram-бота
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Створення об'єкта Bot для доступу до Telegram API
bot = Bot(token=TOKEN)

# 2. Ініціалізація Dispatcher для обробки запитів
dispatcher = Dispatcher(bot, None, workers=0)

# Функція для обробки команди /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привіт! Я бот, який реагує на команду /start!")

# Додавання обробника команди /start
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

# 3. Обробка вебхука
@app.post("/webhook")
async def webhook(request: Request):
    json_str = await request.json()
    update = Update.de_json(json_str, bot)
    dispatcher.process_update(update)
    return {"status": "ok"}

# 4. Налаштування вебхука при запуску сервера
@app.on_event("startup")
async def on_startup():
    webhook_url = "https://game-noab.onrender.com/webhook"  # Замініть на URL вашого сервера
    bot.set_webhook(url=webhook_url)
