from tkinter import *
import time

w = 800
h = 600

window = Tk()
window.title("Moving Ball")
window.resizable(False,False)
canv = Canvas(window, width = w, height = h)
canv.pack()

ball = canv.create_oval(10,10,60,60, fill = "red")

ySpeed = 2
xSpeed = 2.5

while True:
    canv.move(ball,xSpeed,ySpeed)
    p = canv.coords(ball)
    if p[3] >= h or p[1] <= 0:
        ySpeed =- ySpeed
    if p[2] >= w or p[0] <= 0:
        xSpeed =- xSpeed
    window.update()
    time.sleep(0.01)

window.mainloop()
