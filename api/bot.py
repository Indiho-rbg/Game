from fastapi import FastAPI, Request
from telegram import Update, Bot, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Dispatcher, CommandHandler, CallbackContext
import os

app = FastAPI()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("🎮 Начать игру")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Привет! 👋 Готов сыграть в увлекательную игру?", 
        reply_markup=reply_markup
    )

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

@app.post("/webhook")
async def webhook(request: Request):
    json_str = await request.json()
    update = Update.de_json(json_str, bot)
    dispatcher.process_update(update)
    return {"status": "ok"}

@app.on_event("startup")
async def on_startup():
    webhook_url = "https://game-noab.onrender.com/webhook"
    bot.set_webhook(url=webhook_url)
