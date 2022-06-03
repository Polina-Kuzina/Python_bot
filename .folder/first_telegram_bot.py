from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pytube
from pytube import YouTube
from bot_commands import *

app = ApplicationBuilder().token('5468425085:AAEXTChAQ-k3UC6cDYi7NJgae4pSn3IFr4s').build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler('save', save_video))
# app.add_handler(CommandHandler("weather", get_weather))

print('server start')
app.run_polling(stop_signals=None)