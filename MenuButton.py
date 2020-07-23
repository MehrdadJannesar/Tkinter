
# Option and Description

# Menu


from tkinter import *

top = Tk()

mb = Menubutton(top, text = "MenuButton_1", relief = RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb["menu"] = mb.menu

submenu_1 = IntVar()
submenu_2 = IntVar()

mb.menu.add_checkbutton(label = "submenu_1", variable = submenu_1)
mb.menu.add_checkbutton(label = "submenu_2", variable = submenu_2)

mb.pack()
mainloop()
