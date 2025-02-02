from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

# Функція, що запускає гру
def start(update, context):
    # Створюємо кнопку, яка відкриє Web App
    keyboard = [
        [InlineKeyboardButton("Почати гру", web_app="https://game-three-puce.vercel.app/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Відправляємо повідомлення з кнопкою
    update.message.reply_text('Ласкаво просимо до гри!', reply_markup=reply_markup)

def main():
    # Вставте свій токен, який ви отримали від BotFather
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    # Додаємо обробник команд
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Запускаємо бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
