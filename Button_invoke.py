from tkinter import *
from tkinter import messagebox

top = Tk()

def btn_1_click():
    messagebox.showinfo("Message button 1", "BTN_1")

def btn_2_click():
    button1.invoke()

button1 = Button(top, text = "BTN 1", command = btn_1_click)
button1.pack()

button2 = Button(top, text = "BTN 2", command = btn_2_click)
button2.pack()

mainloop()
