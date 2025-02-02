from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Ваш токен Telegram бота
TOKEN = '7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU'

# Функція, яка обробляє команду /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привіт! Я твій бот.')

# Головна функція для обробки запитів
def handler(request):
    if request.method == "POST":
        # Тут ви можете додати код для обробки запиту, наприклад запуск бота
        updater = Updater(TOKEN, use_context=True)
        updater.dispatcher.add_handler(CommandHandler("start", start))
        updater.start_polling()
        return "OK"
    return "Error"
