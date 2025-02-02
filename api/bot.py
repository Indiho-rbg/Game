from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, Updater

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привіт! Я працюю!")

def handler(request):
    token = '7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU'
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    return "OK"
