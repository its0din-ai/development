import socket

host = 'localhost'
inputPerintah = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 666))
print("Program Komunikasi tentang Data Diri")
while inputPerintah.lower() != "keluar":
    inputPerintah = str(input("Apa Perintahnya => "))
    s.send(inputPerintah.encode())
    if inputPerintah.lower() == "keluar":
        respon = s.recv(1024).decode()
        print("Jawab: ",respon)
        s.close()
        break
    elif inputPerintah.lower() != "keluar":
        respon = s.recv(1024).decode()
        print("Jawab: ",respon)
s.close()