# Checkbutton(master , option = value , ....)

# Option and Description

# activebackground --> Background color when the button is under the cursor
# activefoureground --> Foreground color when the button is under the cursor
# bg --> Normal background color
# bd --> Border width in pixels. Default == 2
# fg --> Normal Foreground (Text) color
# command --> Function or method to be called when the button is click
# cursor --> if tou set this option to a cursor name (arrow, dot, hand, etc)
# -----> the mouse cursor will change to that pattern when it is over the checbutton
# font --> Text font to be used for the button's label
# height --> Height of the Button
# width --> Width of the button
# offvalue --> 0 ( disable ) --> Default
# on value --> 1 ( enable )--> Default
# image --> image to be displayed on the Button
# justify --> Left or Right or Center --> How to show multiple text lines
# padx --> additionla padding left and right of the text
# pady --> additionla padding above and below of the text
# relief --> SUNKNE, RAISED, GROOVE, RIDGE
# selectcolor --> The color of the checkbutton when it is set.
# selectimage --> if you set this option to an image, that image will appear in the checkbutton when it is set.


# StringVar() --> Holds a string; default = ""
# IntVar() --> Holds a integer; default = 0
# DoubleVar() --> Holds a float; default = 0.0
# BooleanVar() --> Holds a boolean; returns 0 for Flase, returns 1 for True


from tkinter import *

top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

c1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height = 5, width = 20)

c2 = Checkbutton(top, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, height = 5, width = 20)

c1.pack()
c2.pack()

top.mainloop()
