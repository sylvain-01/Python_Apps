from tkinter import *
from pytube import YouTube

# Initialize window
root = Tk()
root.geometry("500x250")
root.title("youtube video downloader")
root.config(bg="salmon")

# Create Label
Label(root, text="Youtube Video Downloader", font="aerial 20 bold",
      bg="salmon", fg="gold").pack()

# Create field to enter link
link = StringVar()

Label(root, text="Paste Link Below", font="aerial 15 bold underline",
      bg="salmon", fg="snow").place(x=150, y=60)
link_enter = Entry(root, font="aerial 18", width=30, textvariable=link).place(x=20, y=100)


# Function to start downloading
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text="Downloaded", font="aerial 15").place(x=180, y=210)


Button(root, text="Download", font="aerial 15 bold", bg="red",
       padx=5, bd=10, command=downloader).place(x=170, y=170)


root.mainloop()

