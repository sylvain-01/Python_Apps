from tkinter import *
import time

root = Tk()
root.title("Clock")
root.geometry("420x220")


def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    month = time.strftime("%B")
    day_of_month = time.strftime("%d")

    my_label.config(text=hour + ":" + minute + ":" + second)
    my_label.after(1000, clock)

    my_label2.config(text=day)

    my_label3.config(text=month)

    my_label4.config(text=day_of_month)


def update():
    my_label.config(text="New Text")


my_label = Label(root, text="", font=("Helvetica", 60), fg="green", bg="black")
my_label.pack(fill=X)

my_label2 = Label(root, text="", font=("Helvetica", 30), bg="yellow")
my_label2.pack(fill=X)

my_label3 = Label(root, text="", font=("Helvetica", 30), bg="orange")
my_label3.pack(fill=X)

my_label4 = Label(root, text="", font=("Helvetica", 30), bg="red")
my_label4.pack(fill=X)

clock()

root.mainloop()
