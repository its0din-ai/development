import socket

host = 'localhost'
inputPerintah = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 666))
print("Program Komunikasi tentang Server")
while inputPerintah.lower() != "quit":
    inputPerintah = str(input("Apa Perintahnya => "))
    s.send(inputPerintah.encode())
    if inputPerintah.lower() == "quit":
        respon = s.recv(1024).decode()
        print("Jawab: ",respon)
        s.close()
        break
    elif inputPerintah.lower() != "quit":
        respon = s.recv(1024).decode()
        print("Jawab: ",respon)
s.close()