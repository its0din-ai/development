import socket

host = 'localhost'
port = 666
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind((host, port))
soc.listen()

def hitung(alas, tinggi):
    hasil = alas * tinggi
    strHasil = str("{:g}".format(hasil))
    print(f"hasil => {strHasil}")
    conn.send(strHasil.encode())

def main():
    alas = float(conn.recv(1024).decode())
    tinggi = float(conn.recv(2048).decode())
    print(f"alas => {alas}")
    print(f"tinggi => {tinggi}")
    return hitung(alas, tinggi)


print("[Waiting for Connection]")
conn, addr = soc.accept()
print(f"[Incoming Connection from {addr}] Server Dimulai!")
main()
print("Tugas Selesai!")
print("Server Ditutup!")
soc.close()