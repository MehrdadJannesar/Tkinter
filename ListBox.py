# ListBox(master , option = value , ....)


# Option and Description

# selectmode:
#     Browse
#     Single
#     Multiple
#     Extended

# Yscrollcommand
# Xscrollcommand
from tkinter import *

top = Tk()

lb1 = Listbox(top, selectmode = EXTENDED)

lb1.insert(1, "Python")
lb1.insert(1, "Perl")
lb1.insert(1, "Kotlin")
lb1.insert(1, "PHP")
lb1.insert(1, "C#")
lb1.insert(1, "JAVA")

lb1.pack()
mainloop()
