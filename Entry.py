# Entry(master , option = value , ....)

# Option and Description

# Selectbackground --> The background color to use dispalying selected text.
# Selectborderwidth --> The width of the border to use around selected text. default == 1px
# Selectforeground --> The foreground (Text) color of selected text
# show --> password == *
# xscrollcommand --> scroll

# methods :

# delete (first , last)
# insert (index, "string")
# get () ---> return value

from tkinter import *

top = Tk()

l1 = Label(top, text = "User Name")
l1.pack(side = LEFT)
e1 = Entry(top, bd = 5)
e1.pack(side = RIGHT)

mainloop()
