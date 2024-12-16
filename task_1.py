from tkinter import *
from yt_dlp import YoutubeDL

def hight_quality():
    try:
        url =entry.get()
        ydl_opts={
            'format': 'best',
            'outtmpl':'downloads%(titles)s.%(ext)s'
            }
        with YoutubeDL (ydl_opts) as ydl:
            ydl.download([url])
            print("the video has been downloaded")
    except Exception as e:
        print("error dowenloading")


def low_quality():
    try:
        url =entry.get()
        ydl_opts={
            'format': 'worest',
            'outtmpl':'downloads%(titles)s.%(ext)s'
            }
        with YoutubeDL (ydl_opts) as ydl:
            ydl.download([url])
            print("the video has been downloaded")
    except Exception as e:
        print("error dowenloading")        

        
def get_audio():
    try:
        url =entry.get()
        ydl_opts={
            'format': 'audio',
            'outtmpl':'downloads%(titles)s.%(ext)s'
            }
        with YoutubeDL (ydl_opts) as ydl:
            ydl.download([url])
            print("the video has been downloaded")
    except Exception as e:
        print("error dowenloading")
window = Tk()
window.title("youtube")
window.geometry("600x400")
window.configure(bg= "#838B8B")
label = Label(window, text="add your youtube link here", font="bold",bg=window['bg'])
label.place(x=200,y=30)
label.pack()
entry = Entry(window,width=50)
entry.place(x=150, y=100)
high  = Button(window,text="High Quality",command=hight_quality, font="bold", activeforeground="green")
high.place(x=100, y=200)
low = Button(window,text="Low Quality",command=low_quality,font="bold", activeforeground="red")
low.place(x=250, y=200)
audio = Button(window,text="audio only",command=get_audio , font="bold", activeforeground="blue")
audio.place(x=400, y=200)
window.mainloop()

