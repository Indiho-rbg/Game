from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
import os

# Функція для команди /start
async def start(update: Update, context: CallbackContext) -> None:
    game_url = "https://game-three-puce.vercel.app/"  # Замініть на URL вашої гри
    keyboard = [[InlineKeyboardButton("Play Simple Game", url=game_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привіт! Натисніть на кнопку нижче, щоб грати:', reply_markup=reply_markup)

# Основна функція для запуску бота
async def main() -> None:
    token = os.getenv('7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU')  # Отримайте токен з середовища
    
    # Створення аплікації
    application = Application.builder().token(token).build()
    
    # Додавання обробників команд
    application.add_handler(CommandHandler("start", start))
    
    # Запуск бота
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
