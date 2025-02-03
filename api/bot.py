from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функція для команди /start
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    game_url = "https://game-three-puce.vercel.app"  # URL вашої гри
    keyboard = [[InlineKeyboardButton("Play Farm Game", url=game_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привіт! Натисніть на кнопку нижче, щоб грати:', reply_markup=reply_markup)

# Основна функція для запуску бота
def main() -> None:
    # Введіть токен вашого бота тут
    token = '7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU'
    
    # Створення апдейтера і диспетчера
    updater = Updater(token)
    
    dispatcher = updater.dispatcher
    
    # Додавання обробників команд
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
