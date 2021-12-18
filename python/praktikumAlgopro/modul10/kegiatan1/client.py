import socket

host = 'localhost'
port = 666

inputPerintah = ""
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host, port))
print("Program Komunikasi tentang Data Diri")
while inputPerintah.lower() != "keluar":
    inputPerintah = str(input("Apa Perintahnya => "))
    soc.send(inputPerintah.encode())
    if inputPerintah.lower() == "keluar":
        respon = soc.recv(1024).decode()
        print("Jawab: ",respon)
        soc.close()
        break
    elif inputPerintah.lower() != "keluar":
        respon = soc.recv(1024).decode()
        print("Jawab: ",respon)
soc.close()