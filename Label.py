# Label(master , option = value , ....)

# Option and Description

# anchor --> default == Ceneter
# bitmap --> Set this option equal to a bitmap or image object and the label will display that graphic

from tkinter import *

root = Tk()

var = StringVar()

label = Label(root, textvariable = var, relief = RAISED)

var.set("Hey !? How are you doing ?")

label.pack()
root.mainloop()
