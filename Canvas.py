from tkinter import *

top = Tk()

c = Canvas(top, bg = "blue", height = 250, width = 300)
# (x0,y0,x1,y1,.....,xn,yn)
coord = 10 ,50 ,240, 210

arc = c.create_arc(coord, start = 0, extent = 150, fill = "red")
line = c.create_line(10, 10, 200, 200, fill = "white")

c.pack()

mainloop()
