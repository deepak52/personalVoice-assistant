from tkinter import *

from main import run_assistant

root = Tk()
root.geometry('100x100')

btn = Button(root, text="Button", command=run_assistant())

btn.pack()
root.mainloop()
