import socket

host = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((host, 666))
alas = ""
tinggi = ""
print("Menghitung Luas Jajar Genjang")
alas = input("Berapakah Alasnya => ")
s.send(alas.encode())
print(f"[Sudah Dicatat] Alas Jajar Genjang = {alas}\n")
tinggi = input("Berapa Tingginya => ")
s.send(tinggi.encode())
print(f"[Sudah Dicatat] Tinggi Jajar Genjang = {tinggi}")
print("------------------------------------------------")
hasil = s.recv(1024).decode()
print(f"""Hasil kalkulasi Luas Jajar Genjang
dengan tinggi {tinggi} dan alas {alas} adalah => {hasil}
""")