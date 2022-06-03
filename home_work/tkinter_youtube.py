from tkinter import *
import pytube
from pytube import YouTube

def get_video():
    global vid
    global path
    vid = entry_youtube.get()
    path = entry_save.get()
    # print(vid)
    # print(path)
    yt = YouTube(vid)
    yt.streams.filter(progressive=True, file_extension='mp4')
    yt.streams.order_by('resolution')
    yt.streams.desc()
    yt.streams.first().download(path)


window = Tk()
window.title('Приложение для скачивания')
lbl = Label(text = "Привет! Я помогу тебе скачать любое видео с YouTube!\n")
# lbl.grid(column=20, row=20) #задаем положение курсора
lbl.pack()
#поле ввода ссылки на видео:
lbl_youtube = Label(text = "Ссылка на видео")
lbl_youtube.pack()
entry_youtube = Entry(width = 80)
entry_youtube.pack()
#поле ввода куда сохранить:
lbl_save = Label(text = "\n Укажите путь к папке, в которую сохранить видео")
entry_save = Entry(window, width = 80)
lbl_save.pack()
entry_save.pack()

# vid1 = entry_youtube.get()
# path1 = entry_save.get()

#кнопка с текстом:
button = Button(text =  "Скачать видео", width = 25, height = 2, bg = "red", fg = "white", command=get_video)
button.pack()
window.mainloop() #бесконечное открытие окна

