import socket, platform

host = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, 666))
s.listen()
print("Server Dimulai!")
dataInput = ""

while dataInput.lower() != "quit":
    koneksi, addr = s.accept()
    while dataInput.lower() != "quit":
        dataInput = koneksi.recv(1024).decode()
        if dataInput.lower() == "quit":
            s.close()
            break
        print("Beri aku Perintah: ", dataInput.lower())
        if dataInput.lower() == "machine":
            data = platform.machine()
            koneksi.send(data.encode())
        elif dataInput.lower() == "release":
            data = platform.release()
            koneksi.send(data.encode())
        elif dataInput.lower() == "system":
            data = platform.system()
            koneksi.send(data.encode())
        elif dataInput.lower() == "version":
            data = platform.version()
            koneksi.send(data.encode())
        elif dataInput.lower() == "node":
            data = platform.node()
            koneksi.send(data.encode())
        else:
            txt = "Unknown Command!"
            koneksi.send(txt.encode())
        