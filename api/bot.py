from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
# Вставте ваш токен сюди
TOKEN = '7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU'

# Функція для команди /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привіт! Я готовий до роботи!')

# Основна функція, яка запускає бота
def main():
    updater = Updater(TOKEN, use_context=True)
    
    # Отримуємо диспетчер для обробки команд
    dp = updater.dispatcher
    
    # Додаємо команду /start
    dp.add_handler(CommandHandler("start", start))
    
    # Запускаємо бота
    updater.start_polling()

    # Додаємо обробку сигнала для зупинки бота
    updater.idle()

if __name__ == '__main__':
    main()
