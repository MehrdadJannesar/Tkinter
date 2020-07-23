# add_command() --> adds a menu item to the menu
# add_radionbutton() --> Creates a radio button menu item
# add_checkbutton() --> Creates a check button menu item
# add_cascade()

from tkinter import *

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text = "Do Nothing Button" )
    button.pack()

root = Tk()
root.title("Test Menu")
root.geometry("400x400")
# root.resizable(False, False)
root.wm_withdraw()
print(root.state())
root.wm_deiconify()
print(root.state())
menubar = Menu(root)
# file
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = donothing)
filemenu.add_command(label = "Open", command = donothing)
filemenu.add_command(label = "Save", command = donothing)
filemenu.add_command(label = "Save as...", command = donothing)
filemenu.add_command(label = "Close", command = donothing)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)
# edit
editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label = "Undo", command = donothing)
editmenu.add_separator()
editmenu.add_command(label = "Cut", command = donothing)
editmenu.add_command(label = "Copy", command = donothing)
editmenu.add_command(label = "Paste", command = donothing)
editmenu.add_command(label = "Delete", command = donothing)
editmenu.add_command(label = "Select All", command = donothing)

menubar.add_cascade(label = "Edit", menu = editmenu)


# help
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "About", command = donothing)
helpmenu.add_command(label = "Help Index", command = donothing)
menubar.add_cascade(label = "Help", menu = helpmenu)

root.config(menu = menubar)
root.mainloop()
