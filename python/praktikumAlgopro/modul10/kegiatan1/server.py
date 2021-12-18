import socket

host = 'localhost'
port = 666

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((host, port))
soc.listen()
print("Server Dimulai!")
dataInput = ""
dataBase = {
    "nama" : "MUHAMMAD WAHYU SYAFI'UDDIN",
    "nim" : "L200210056",
    "angkatan" : "2021",
    "keluar" : "Siap!"
}

while dataInput.lower() != "keluar":
    koneksi, addr = soc.accept()
    while dataInput.lower() != "keluar":
        dataInput = koneksi.recv(1024).decode()
        if dataInput.lower() == "keluar":
            data = dataBase["keluar"]
            koneksi.send(data.encode())
            soc.close()
            break
        print("Beri aku Perintah: ", dataInput.lower())
        if dataInput.lower() in dataBase:
            data = dataBase[dataInput.lower()]
            koneksi.send(data.encode())
        else:
            txt = "Perintah tidak dimengerti, tuan!"
            koneksi.send(txt.encode())
        