from tkinter import Tk, Label, Entry, Button, StringVar

gui3 = Tk(className="Luas Geometri")
gui3.geometry("850x400")

judul = Label(gui3, text="Luas Jajar Genjang", font=("Poppins", 20, "bold")).place(x=20, y=20)
desk = Label(gui3, text="""Jajar genjang atau jajaran genjang adalah bangun datar dua dimensi yang dibentuk oleh
dua pasang rusuk yang masing-masing sama panjang dan sejajar dengan pasangannya,
dan memiliki dua pasang sudut yang masing-masing sama besar dengan sudut di hadapannya.""", font=("Poppins", 10, "bold"), justify="left").place(x=20, y=60)

teksPar1 = Label(gui3, text="Panjang Alas: ").place(x=20, y=120)
alas = StringVar()
entPar1 = Entry(gui3, textvariable=alas).place(x=130, y=120)

teksPar2 = Label(gui3, text="Panjang Tinggi: ").place(x=20, y=150)
tinggi = StringVar()
entPar2 = Entry(gui3, textvariable=tinggi).place(x=130, y=150)

def luas():
    luas = int(alas.get()) * int(tinggi.get())
    hasil = Label(gui3, text=("LUAS =")).place(x=120, y=205)
    hasil = Label(gui3, text=str(luas)).place(x=175, y=205)
    return hasil

butLuas = Button(gui3, text="Hitung", command=luas).place(x=20, y=200)

gui3.mainloop()

# DONE