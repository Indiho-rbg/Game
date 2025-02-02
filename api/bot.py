import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Dispatcher
from flask import Flask, request

TOKEN = '7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU'

# Налаштовуємо Flask
app = Flask(__name__)

# Ініціалізуємо Telegram бота
updater = Updater(TOKEN, use_context=True)
dispatcher: Dispatcher = updater.dispatcher

# Функція для обробки команди /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привіт! Я бот!")

dispatcher.add_handler(CommandHandler("start", start))

# Вебхук для отримання оновлень від Telegram
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = Update.de_json(json_str, updater.bot)
    dispatcher.process_update(update)
    return 'OK', 200

# Встановлюємо вебхук при завантаженні
updater.bot.setWebhook(f'https://game-three-puce.vercel.app/{TOKEN}')

# Головна сторінка для перевірки роботи
@app.route('/')
def home():
    return "Bot is running!", 200

# ВАЖЛИВО! Це потрібно для Vercel
handler = app
