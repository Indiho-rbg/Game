from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

# Введи свій токен
TOKEN = '7592348192:AAFyqIJnZTvjjzShu_az9emIKZKkkZFcQFk'

def start(update: Update, context: CallbackContext):
    # Визначаємо кнопку, яка відкриє веб-додаток
    keyboard = [
        [
            InlineKeyboardButton("Start Game", web_app=WebAppInfo(url="https://game-three-puce.vercel.app/"))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Відправляємо повідомлення з кнопкою
    update.message.reply_text("Привіт! Натисни кнопку, щоб почати гру!", reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Додаємо команду /start
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
