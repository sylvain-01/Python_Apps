from tkinter import *
import base64

# Initialize window
root = Tk()
root.geometry("590x540")
root.title("Encode & Decode Messages")
root.config(bg="light blue")

# Label
Label(root, text="Encode & Decode Messages", font="aerial 25 italic", bg="light blue").pack()

# Define variables
Text = StringVar()
private_key = StringVar()
Mode = StringVar()
Result = StringVar()


# Function to encode
def encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Function to decode
def decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

    return "".join(dec)


# Function to set mode
def mode():
    if Mode.get() == "e":
        Result.set(encode(private_key.get(), Text.get()))
    elif Mode.get() == "d":
        Result.set(decode(private_key.get(), Text.get()))
    else:
        Result.set("Invalid Mode")


# Function to exit
def close():
    root.destroy()


# Function to reset
def reset():
    Text.set("")
    private_key.set("")
    Mode.set("")
    Result.set("")


# Labels & Buttons
Label(root, font="aerial 15 bold", bg="light blue", text="MESSAGE").place(x=15, y=75)
Entry(root, font="aerial 18", textvariable=Text, bg="snow").place(x=75, y=105)

Label(root, font="aerial 15 bold", bg="light blue", text="ENTER KEY").place(x=15, y=165)
Entry(root, font="aerial 18", textvariable=private_key, bg="snow").place(x=75, y=195)

Label(root, font="aerial 15 bold", bg="light blue", text="MODE (e-encode, d-decode)").place(x=15, y=275)
Entry(root, font="aerial 18", textvariable=Mode, bg="snow").place(x=75, y=305)
Entry(root, font="aerial 18", textvariable=Result, bg="snow").place(x=195, y=390)

Button(root, font="aerial 15 bold", text="RESULT", padx=2, width=6, bg="lime green",
       bd=5, command=mode).place(x=35, y=390)
Button(root, font="aerial 12 bold", text="RESET", padx=2, width=6, bg="orange2",
       bd=5, command=reset).place(x=0, y=495)
Button(root, font="aerial 12 bold", text="EXIT", padx=2, width=6, bg="red",
       bd=5, command=close).place(x=500, y=495)


root.mainloop()

