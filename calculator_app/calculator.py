import tkinter

# Create window from tkinter module
window = tkinter.Tk()
window.title("Calculator")
window.geometry("370x440")


expression = " "


# Create functions
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)


def clear():
    global expression
    expression = " "
    label_result.config(text=expression)


def calculate():
    global expression
    result = " "
    if expression != " ":
        try:
            result = eval(expression)
        except:
            result = "ERROR"
            expression = " "
    label_result.config(text=result)


# Create GUI
label_result = tkinter.Label(window, text="")
label_result.grid(row=0, column=0, columnspan=4)
label_result.config(height=2)
label_result.config(font=("courier", 30))

button_1 = tkinter.Button(window, text="1", command=lambda: add("1"))
button_1.grid(row=1, column=0)
button_1.config(width=4, height=2)
button_1.config(font=("courier", 20))

button_2 = tkinter.Button(window, text="2", command=lambda: add("2"))
button_2.grid(row=1, column=1)
button_2.config(width=4, height=2)
button_2.config(font=("courier", 20))


button_3 = tkinter.Button(window, text="3", command=lambda: add("3"))
button_3.grid(row=1, column=2)
button_3.config(width=4, height=2)
button_3.config(font=("courier", 20))

button_divide = tkinter.Button(window, text="/", command=lambda: add("/"))
button_divide.grid(row=1, column=3)
button_divide.config(width=4, height=2)
button_divide.config(font=("courier", 20))

button_4 = tkinter.Button(window, text="4", command=lambda: add("4"))
button_4.grid(row=2, column=0)
button_4.config(width=4, height=2)
button_4.config(font=("courier", 20))

button_5 = tkinter.Button(window, text="5", command=lambda: add("5"))
button_5.grid(row=2, column=1)
button_5.config(width=4, height=2)
button_5.config(font=("courier", 20))

button_6 = tkinter.Button(window, text="6", command=lambda: add("6"))
button_6.grid(row=2, column=2)
button_6.config(width=4, height=2)
button_6.config(font=("courier", 20))

button_multiply = tkinter.Button(window, text="*", command=lambda: add("*"))
button_multiply.grid(row=2, column=3)
button_multiply.config(width=4, height=2)
button_multiply.config(font=("courier", 20))

button_7 = tkinter.Button(window, text="7", command=lambda: add("7"))
button_7.grid(row=3, column=0)
button_7.config(width=4, height=2)
button_7.config(font=("courier", 20))

button_8 = tkinter.Button(window, text="8", command=lambda: add("8"))
button_8.grid(row=3, column=1)
button_8.config(width=4, height=2)
button_8.config(font=("courier", 20))

button_9 = tkinter.Button(window, text="9", command=lambda: add("9"))
button_9.grid(row=3, column=2)
button_9.config(width=4, height=2)
button_9.config(font=("courier", 20))

button_subtract = tkinter.Button(window, text="-", command=lambda: add("-"))
button_subtract.grid(row=3, column=3)
button_subtract.config(width=4, height=2)
button_subtract.config(font=("courier", 20))

button_clear = tkinter.Button(window, text="C", command=lambda: clear())
button_clear.grid(row=4, column=0)
button_clear.config(width=4, height=2)
button_clear.config(font=("courier", 20))

button_0 = tkinter.Button(window, text="0", command=lambda: add("0"))
button_0.grid(row=4, column=1)
button_0.config(width=4, height=2)
button_0.config(font=("courier", 20))

button_dot = tkinter.Button(window, text=".", command=lambda: add("."))
button_dot.grid(row=4, column=2)
button_dot.config(width=4, height=2)
button_dot.config(font=("courier", 20))

button_add = tkinter.Button(window, text="+", command=lambda: add("+"))
button_add.grid(row=4, column=3)
button_add.config(width=4, height=2)
button_add.config(font=("courier", 20))

button_equals = tkinter.Button(window, text="=", command=lambda: calculate())
button_equals.grid(row=5, column=0, columnspan=4)
button_equals.config(width=21, height=2)
button_equals.config(font=("courier", 20))


# Create Color
myWidgets = [button_0, button_1, button_2, button_3,button_4,
             button_5, button_6, button_7, button_8, button_9,
             button_clear, button_dot]
for window in myWidgets:
    window.configure(bg="yellow")


myWidgets2 = [button_add, button_subtract,button_multiply,
              button_equals, button_divide]
for window in myWidgets2:
    window.configure(bg="white")


window.mainloop()
