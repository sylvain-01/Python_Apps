from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Initialize window
root = Tk()
root.geometry("1535x535")
root.config(bg="mint cream")
root.title("Language Translator")

Label(root, text="Language Translator", font="roman 20 bold",
      bg="mint cream").pack()

# Create input-output widget
Label(root, text="Enter Text", font="aerial 17 bold",
      bg="old lace").place(x=25, y=90)

input_text = Text(root, font="aerial 15", height=11, wrap=WORD,
                  padx=5, pady=5, width=60, bg="old lace")
input_text.place(x=20, y=120)

Label(root, text="Output", font="aerial 17 bold",
      bg="snow2").place(x=740, y=90)

output_text = Text(root, font="aerial 15", height=11, wrap=WORD,
                   padx=5, pady=5, width=60, bg="snow2")
output_text.place(x=720, y=120)

# Define combobox to select the language
language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values=language, width=22, font="aerial 15")
src_lang.place(x=205, y=90)
src_lang.set("choose input language")

dest_lang = ttk.Combobox(root, values=language, width=22, font="aerial 15")
dest_lang.place(x=920, y=90)
dest_lang.set("choose output language")


# Define function
def translate():
    translator = Translator()
    translated = translator.translate(text=input_text.get(1.0, END),
                                      src=src_lang.get(), dest=dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)


trans_btn = Button(root, text="Translate", font="aerial 12 bold",
                   pady=5, command=translate, bg="cornflower blue",
                   activebackground="cyan", bd=12)
trans_btn.place(x=650, y=435)


root.mainloop()

