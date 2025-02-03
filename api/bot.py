import os
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = f"https://game-noab.onrender.com"

app = FastAPI()

async def start(update: Update, context):
    await update.message.reply_text("Привіт! Я бот на Render!")

# Ініціалізація бота
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

@app.on_event("startup")
async def set_webhook():
    await application.bot.set_webhook(WEBHOOK_URL)

@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, application.bot)
    await application.update.update_queue.put(update)
    return JSONResponse({"status": "ok"})
