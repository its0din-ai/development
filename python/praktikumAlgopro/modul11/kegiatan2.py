from tkinter import Tk, Label, Entry, Button, StringVar

gui2 = Tk(className="Kalkulator Sederhana")
gui2.geometry("854x550")

labAngka1 = Label(gui2, text="ANGKA 1")
labAngka1.grid(padx=(250, 10), pady=80, sticky = "W", row=0, column=0)

angka1 = StringVar()
entryAngka1 = Entry(gui2, textvariable=angka1, justify="right")
entryAngka1.grid(sticky = "W", row=0, column=1, ipady=20, ipadx=40)


labAngka2 = Label(gui2, text="ANGKA 2")
labAngka2.grid(padx=(250, 10), sticky = "W", row=1, column=0)

angka2 = StringVar()
entryAngka2 = Entry(gui2, textvariable=angka2, justify="right")
entryAngka2.grid(sticky = "W", row=1, column=1, ipady=20, ipadx=40)

def tambah():
    kalkulasi = int(angka1.get()) + int(angka2.get())
    hasil = Label(gui2, text=("HASIL")).grid(padx=(0, 10), sticky = "E", row=4, column=0)
    hasil = Label(gui2, text=str(kalkulasi)).grid(padx=(0, 10), sticky = "E", row=4, column=1)
    return hasil

def kurang():
    kalkulasi = int(angka1.get()) - int(angka2.get())
    hasil = Label(gui2, text=("HASIL")).grid(padx=(0, 10), sticky = "E", row=4, column=0)
    hasil = Label(gui2, text=str(kalkulasi)).grid(padx=(0, 10), sticky = "E", row=4, column=1)
    return hasil

def kali():
    kalkulasi = int(angka1.get()) * int(angka2.get())
    hasil = Label(gui2, text=("HASIL")).grid(padx=(0, 10), sticky = "E", row=4, column=0)
    hasil = Label(gui2, text=str(kalkulasi)).grid(padx=(0, 10), sticky = "E", row=4, column=1)
    return hasil

def bagi():
    kalkulasi = int(angka1.get()) / int(angka2.get())
    hasil = Label(gui2, text=("HASIL")).grid(padx=(0, 10), sticky = "E", row=4, column=0)
    hasil = Label(gui2, text=str(kalkulasi)).grid(padx=(0, 10), sticky = "E", row=4, column=1)
    return hasil

plus = Button(gui2, text="+", command=tambah)
plus.grid(row=3, column=0, sticky="W", padx=(250, 0), pady=80, ipadx=15, ipady=15)

mins = Button(gui2, text="-", command=kurang)
mins.grid(row=3, column=1, sticky="W", padx=(40, 0), pady=80, ipadx=15, ipady=15)

mult = Button(gui2, text="X", command=kali)
mult.grid(row=3, column=1, sticky="W", padx=(150, 0), pady=80, ipadx=15, ipady=15)

divs = Button(gui2, text=":", command=bagi)
divs.grid(row=3, column=2, sticky="W", padx=(0, 0), pady=80, ipadx=15, ipady=15)

gui2.mainloop()