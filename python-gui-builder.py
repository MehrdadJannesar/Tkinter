import tkinter as tk
from tkinter import ttk
from tkinter import *

# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = tInput.get()
	return userInput


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')



root = Tk()

# This is the section of code which creates the main window
root.geometry('462x374')
root.configure(background='#7FFFD4')
root.title('Hello!')


# This is the section of code which creates a button
Button(root, text='Click me!', bg='#98F5FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=181, y=310)


# This is the section of code which creates a text input box
tInput=Entry(root)
tInput.place(x=161, y=260)


# This is the section of code which creates a button
Button(root, text='Button text!', bg='#98F5FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=276, y=310)


root.mainloop()
