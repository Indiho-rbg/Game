from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

# Твій токен
TOKEN = '7592348192:AAFyqIJnZTvjjzShu_az9emIKZKkkZFcQFk'

def start(update: Update, context: CallbackContext):
    # Створюємо кнопку з Web App
    keyboard = [
        [
            InlineKeyboardButton("Start Game", web_app=WebAppInfo(url="https://game-git-main-indihos-projects.vercel.app/"))
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Відправляємо повідомлення з кнопкою
    update.message.reply_text("Привіт! Натисни кнопку, щоб почати гру!", reply_markup=reply_markup)

def main():
    # Створюємо апдейтера та диспетчера
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Обробляємо команду /start
    dp.add_handler(CommandHandler("start", start))

    # Починаємо опитування
    updater.start_polling()

    # Залишаємо бот активним
    updater.idle()

if __name__ == '__main__':
    main()
