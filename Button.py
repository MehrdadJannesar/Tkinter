# Button(master , option = value , ....)

# master --> This represents the parent window



# Option and Description

# activebackground --> Background color when the button is under the cursor
# activefoureground --> Foreground color when the button is under the cursor
# bg --> Normal background color
# bd --> Border width in pixels. Default == 2
# fg --> Normal Foreground (Text) color
# command --> Function or method to be called when the button is click
# font --> Text font to be used for the button's label
# height --> Height of the Button
# width --> Width of the button
# image --> image to be displayed on the Button
# justify --> Left or Right or Center --> How to show multiple text lines
# padx --> additionla padding left and right of the text
# pady --> additionla padding above and below of the text
# relief --> SUNKNE, RAISED, GROOVE, RIDGE
# state --> DISABLED, NORMAL, ACTIVE

from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")

def helloCallBack():
    msg = messagebox.showinfo("info", "Hello tkinter!")

b = Button(top, text = "Test", command = helloCallBack, state = "disable")
b.pack()

top.mainloop()
