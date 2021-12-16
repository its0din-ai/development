import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 666))
s.listen(5)
print("Koneksi [200] OK")
dataInput = ""
dataBase = {
    "nama" : "ODIN Ryuji",
    "nim" : "L200210056",
    "angkatan" : "2021",
    "keluar" : "Siap!"
}

while dataInput.lower() != "keluar":
    koneksi, addr = s.accept()
    while dataInput.lower() != "keluar":
        dataInput = koneksi.recv(1024)
        if dataInput.lower() == "keluar":
            s.close()
            break
        print("Beri aku Perintah: ", dataInput)
        if dataBase.has_key(dataInput):
            koneksi.send(dataBase[dataInput])
        else:
            koneksi.send("Perintah tidak dimengerti, tuan!")
        