from tkinter import Tk, Label, Button
from tkinter.messagebox import showinfo

gui1 = Tk(className="Informasi Data Diri")
judul = Label(gui1, text="Data Diri", font=("Times New Roman", 20, "bold"))
judul.grid(padx=(10, 10), sticky = "W", row=0, column=0)

labNama = Label(gui1, text="NAMA")
labNama.grid(padx=(10, 10), sticky = "W", row=1, column=0)
nama = Label(gui1, text="MUHAMMAD WAHYU SYAFI'UDDIN")
nama.grid(padx=(10, 10), sticky = "W", row=1, column=1)

labNIM = Label(gui1, text="NIM")
labNIM.grid(padx=(10, 10), sticky = "W", row=2, column=0)
nim = Label(gui1, text="L200210056")
nim.grid(padx=(10, 10), sticky = "W", row=2, column=1)

labBuku = Label(gui1, text="BUKU FAVORIT")
labBuku.grid(padx=(10, 10), sticky = "W", row=3, column=0)
buku = Label(gui1, text="YOU DO YOU - Fellexandro Ruby")
buku.grid(padx=(10, 10), sticky = "W", row=3, column=1)

labIdol = Label(gui1, text="IDOLA DIKALANGAN SAHABAT")
labIdol.grid(padx=(10, 10), sticky = "W", row=4, column=0)
idol = Label(gui1, text="Muhammad al-Fatih")
idol.grid(padx=(10, 10), sticky = "W", row=4, column=1)

labMotto = Label(gui1, text="MOTTO")
labMotto.grid(padx=(10, 10), sticky = "W", row=5, column=0)
motto = Label(gui1, text="Cogito Ergo Sum!")
motto.grid(padx=(10, 10), sticky = "W", row=5, column=1)

def tutup():
    gui1.destroy()

tombolTutup = Button(gui1, text="TUTUP", command=tutup)
tombolTutup.grid(sticky = "e", row=10, column=2)

gui1.mainloop()