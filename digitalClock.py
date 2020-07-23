from tkinter import *

from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S')
    lbl.config(text = string)
    # after(delay(milisecond), function)
    lbl.after(1000, time)

lbl = Label(root, font = ('calibri',40,'bold'), bg = "purple", fg = "white")

lbl.pack(anchor = "center")

time()
root.mainloop()
