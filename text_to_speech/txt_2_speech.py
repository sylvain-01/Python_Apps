# import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound


# Create window
root = Tk()
root.geometry("600x300")
root.config(bg="white")
root.title("TEXT TO SPEECH")


# Bottom heading
bottom_label = Label(root, text="text to speech app", font="arial 20 italic",
                     bg="yellow").pack(fill=X, side=BOTTOM)

# Search label
top_label = Label(root, text="ENTER TEXT BELOW", font="arial 20 bold underline",
                  bg="yellow").pack(fill=X, side=TOP)

# Text variable
Msg = StringVar()

# Entry
entry_field = Entry(root, textvariable=Msg, font="aerial 35 bold")
entry_field.pack(fill=X)


# Define function
def text_to_speech():
    message = entry_field.get()
    speech = gTTS(text=message)
    speech.save("test.mp3")
    playsound("test.mp3")


def close():
    root.destroy()


def clear():
    Msg.set("")


# Button
Button(root, text="PLAY", font="arial 25 bold", command=text_to_speech, bg="light green").pack(fill=X)
Button(root, text="CLEAR", font="arial 25 bold", command=clear, bg="orange").pack(fill=X)
Button(root, text="EXIT", font="arial 25 bold", command=close, bg="Red").pack(fill=X)


# Infinite loop to run program
root.mainloop()
