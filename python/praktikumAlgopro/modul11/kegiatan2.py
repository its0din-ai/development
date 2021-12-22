from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter.messagebox import showinfo

gui2 = Tk(className="Kalkulator Sederhana")
labAngka1 = Label(gui2, text="ANGKA 1")
labAngka1.grid(padx=30, pady=30, sticky = "W", row=0, column=0)

angka1 = StringVar()
entryAngka1 = Entry(gui2, textvariable=angka1)
entryAngka1.grid(padx=(10, 10), sticky = "W", row=0, column=1, ipady=15)


labAngka2 = Label(gui2, text="ANGKA 2")
labAngka2.grid(padx=30, pady=10, sticky = "W", row=1, column=0)

angka2 = StringVar()
entryAngka2 = Entry(gui2, textvariable=angka2)
entryAngka2.grid(padx=(10, 10), sticky = "W", row=1, column=1, ipady=15)

# BELUM SELESAI !

gui2.mainloop()