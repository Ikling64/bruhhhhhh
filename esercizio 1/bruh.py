#Import the required libraries
from tkinter import *
import random
root = Tk()

root.geometry("700x350")
root.config(bg='#FF3333')
root.title("test")

def opennewpage(): 
    newwin = Toplevel(root)
    newwin.title("chill")

root.resizable(False, False)
#Create a Label
Label(root, text = "hello").place(relx=.5, rely=.5,anchor=CENTER)
Button(root, text = "Quit", command=opennewpage, relief=RIDGE).place(x=650, y=330, anchor=SW)
root.mainloop()