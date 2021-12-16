import socket

host = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, 666))
s.listen()
print("Server Dimulai!")
dataInput = ""
dataBase = {
    "nama" : "MUHAMMAD WAHYU SYAFI'UDDIN'",
    "nim" : "L200210056",
    "angkatan" : "2021",
    "keluar" : "Siap!"
}

while dataInput.lower() != "keluar":
    koneksi, addr = s.accept()
    while dataInput.lower() != "keluar":
        dataInput = koneksi.recv(1024).decode()
        if dataInput.lower() == "keluar":
            data = dataBase["keluar"]
            koneksi.send(data.encode())
            s.close()
            break
        print("Beri aku Perintah: ", dataInput.lower())
        if dataInput.lower() in dataBase:
            data = dataBase[dataInput.lower()]
            koneksi.send(data.encode())
        else:
            txt = "Perintah tidak dimengerti, tuan!"
            koneksi.send(txt.encode())
        