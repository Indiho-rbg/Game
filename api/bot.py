import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/bot', methods=['POST', 'GET'])
def handle_request():
    return "Bot is running!", 200

# Токен вашого бота
TOKEN = '7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU'

# Функція для обробки команд
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привіт! Я бот!")

# Обробка запиту від Telegram
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = Update.de_json(json_str, updater.bot)
    dispatcher.process_update(update)
    return 'OK'

# Запуск бота
if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Встановлюємо вебхук
    updater.bot.setWebhook(f'https://game-three-puce.vercel.app/{TOKEN}')
    app.run()

    handler = app  # ВАЖЛИВО для Vercel
