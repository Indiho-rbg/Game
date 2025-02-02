# bot.py

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функція для обробки команд
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привіт!')

# Створення обробника команд
def main():
    updater = Updater("YOUR_TOKEN")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

# Головна точка входу
def handler(request):
    main()
    return "Bot is running!"
