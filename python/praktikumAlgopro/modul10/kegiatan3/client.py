import socket

host = 'localhost'
port = 666
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.connect((host, port))

alas = ""
tinggi = ""
print("Menghitung Luas Jajar Genjang")
alas = input("Berapakah Alasnya => ")
soc.send(alas.encode())
print(f"[Sudah Dicatat] Alas Jajar Genjang = {alas}\n")
tinggi = input("Berapa Tingginya => ")
soc.send(tinggi.encode())

print(f"[Sudah Dicatat] Tinggi Jajar Genjang = {tinggi}")
print("------------------------------------------------")
print("Selanjutnya mau ngapain?")
print("""1. Hitung
2. Keluar""")

pilihan = input("Pilihanmu => ").lower()

if pilihan == "hitung" or "1":
    hasil = soc.recv(1024).decode()
    print(f"""Hasil kalkulasi Luas Jajar Genjang
dengan tinggi {tinggi} dan alas {alas} adalah => {hasil}""")
    print("Terimakasih..")
    soc.close()
elif pilihan == "keluar" or "2":
    print("Kembali Lagi yaa..")
    soc.close()
    quit()
else:
    print("Menu Tidak Tersedia")
    print("Silahkan Coba Lagi")
    soc.close()