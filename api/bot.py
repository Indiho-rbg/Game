import logging
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

# Створюємо Flask застосунок
app = Flask(__name__)

# Токен вашого бота
TOKEN = "7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU"

# Створюємо бота
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

# Логування
logging.basicConfig(level=logging.INFO)

# Функція для команди /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привіт! Я бот!")

dispatcher.add_handler(CommandHandler("start", start))

# Обробник запитів від Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = Update.de_json(json_str, bot)
    dispatcher.process_update(update)
    return "OK", 200

# Встановлюємо вебхук при розгортанні
@app.route("/")
def set_webhook():
    url = f"https://game-three-puce.vercel.app/{TOKEN}"
    bot.set_webhook(url)
    return f"Webhook set to {url}", 200

# Головна змінна для Vercel
handler = app
