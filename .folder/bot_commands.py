from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pytube
from pytube import YouTube



async def help_command(update: Update, context: ContextTypes):
    await update.message.reply_text(f'/help - справка по командам \n/hello - приветсвие \n/sum - чтобы узнать сумму 2 чисел, введите /sum и два числа через пробел\n /save - чтобы скачать видео с YouTube отправьте /save + ссылка на видео\n /weather - узнайте прогноз погоды в любом городе')

async def hello(update: Update, context: ContextTypes):
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!')


async def save_video(update: Update, context: ContextTypes):
    global app
    msg = update.message.text
    print(msg) 
    items = msg.split(' ')   
    yt = YouTube(items[1])      
    yt.streams.filter(progressive=True, file_extension='mp4')
    yt.streams.order_by('resolution')
    yt.streams.desc()
    yt.streams.first().download(output_path=r"C:\Users\payli\Downloads\Bot_telegram", filename='yt_video.mp4'
)
    video = open(r"C:\Users\payli\Downloads\Bot_telegram\yt_video.mp4", 'rb') 
    # app.send_video(update.message.chat.id, video)
    await update.message.reply_video(video)

async def sum_command(update: Update, context: ContextTypes):
    global app
    msg = update.message.text
    print(msg) 
    items = msg.split(' ')
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}') 

