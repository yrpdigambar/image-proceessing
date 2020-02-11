from tkinter import *
from tkinter import filedialog
a=Tk()

def mfileopen():
    file1 = filedialog.askopenfile(initialdir="/", title="select file", filetypes=(("text files",".jpeg,.pnj,.jpg"),("all files","*.*")))
    label = Label(text=file1).pack()


button= Button(text="open file",width = 30, command=mfileopen).pack()
a.mainloop()
