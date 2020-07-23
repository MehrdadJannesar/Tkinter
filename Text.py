from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello......")
text.insert(END, "Bye Bye.......")

text.pack()

# tag_add(tagname, start index, end index)
###########################
text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background = "yellow", foreground = "blue")
text.tag_config("start", background = "black", foreground = "green")
##############################
# tag_delete(tagname)
# text.tag_delete("here")
#################################

# text.tag_remove(tagname, start index, stop index)
text.tag_remove("start", "1.9", "1.11")
############################
mainloop()
