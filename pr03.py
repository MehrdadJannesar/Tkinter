from tkinter import *

# binding --> click (keyboard or mouse)
# lambda --> Quick function

win = Tk()

def go():
    cs = lb.curselection()[0] # --> tupel(0,1)
    label['text'] = lb.get(cs)

lb = Listbox(win)
lb.bind("<<ListboxSelect>>", lambda x: go())
# label.bind("<Button-3>", function)
lb.pack()

items = ["first", "sec", "third"]

for item in items:
    lb.insert(END, item)

label = Label(win)
label.pack()
# label(master, option, #text = )
mainloop()
