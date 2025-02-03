import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# Налаштування логування
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Токен вашого бота
TOKEN = '7592348192:AAGE24v6WWSKRSIclap7iUATad5kqdimYSU'

# Функція для обробки команд
async def start(update: Update, context: CallbackContext):
    logging.info(f"Received /start command from {update.message.chat_id}")
    await update.message.reply_text("Привіт! Я бот!")

# Створення та налаштування бота
application = Application.builder().token(TOKEN).build()
dispatcher = application.dispatcher
dispatcher.add_handler(CommandHandler("start", start))

# Обробка запиту від Telegram
@app.post(f'/{TOKEN}')
async def webhook(request: Request):
    json_str = await request.json()  # Виправлено на json() замість декодування вручну
    update = Update.de_json(json_str, application.bot)
    dispatcher.process_update(update)
    return JSONResponse({"status": "ok"})

# Встановлення вебхука для бота
application.bot.set_webhook(f'https://game-three-puce.vercel.app/{TOKEN}')

# Запуск FastAPI сервера
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
