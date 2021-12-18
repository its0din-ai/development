import socket
host = 'localhost'
port = 666
inputPerintah = ""
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host, port))
print("Program Komunikasi tentang Server")
while inputPerintah.lower() != "quit":
    inputPerintah = str(input("Apa Perintahnya => "))
    soc.send(inputPerintah.encode())
    if inputPerintah.lower() == "quit":
        respon = soc.recv(1024).decode()
        print("Jawab: ",respon)
        soc.close()
        break
    elif inputPerintah.lower() != "quit":
        respon = soc.recv(1024).decode()
        print("Jawab: ",respon)
soc.close()