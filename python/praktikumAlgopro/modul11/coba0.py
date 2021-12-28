from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter.messagebox import showinfo

myApp = Tk(className="Akses terhadap Widget")

l1 = Label(myApp, text="ODIN")
l1.grid(row=0, column=0)
str1 = StringVar()
e1 = Entry(myApp, textvariable=str1)
l2 = Label(myApp, text="Umur")
l2.grid(row=1, column=0)
str2 = StringVar(value=0)
e2 = Entry(myApp, textvariable=str2)
e2.grid(row=1, column=1)

def info():
    _info = str1.get()+' Berumur'+str2.get()+' Tahun'
    showinfo('Pesan', _info)

def hapus(): 
    str1.set('')
    str2.set(0)

b1 = Button(myApp, text="Informasi", command=info)
b1.grid(row=2, column=1)
b2 = Button(myApp, text="Hapus", command=hapus)
b2.grid(row=2, column=0)

myApp.mainloop()

# UNDERSTOOD