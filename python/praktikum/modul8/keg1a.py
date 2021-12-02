# Praktikum Modul 8 - Membuat Modul
# Oleh, Muhammad Wahyu Syafi'uddin
# NIM : L200210056

# Statement
data = {"NIM":"L200210056",
        "NAMA":"MUHAMMAD WAHYU SYAFI'UDDIN",
        "ALAMAT":"KLATEN, JAWA TENGAH",
        "POST":"57482",
        "PRODI":"TEKNIK INFORMATIKA",
        "KELAS":"PRAKTIKUM ALGOPRO B",
        "EMAIL":"l200210056@student.ums.ac.id"
        }

# Function / Module
def bantuan():
    print("+------------------------------+")
    print("""| Untuk Menampilkan Informasi  |
| Harap Masukkan Kode Angkanya |""")
    print("+------------------------------+")
    print("Pilihan yang tersedia :")
    print("""b Menampilkan bantuan ini
N Menampilkan NIM
a Menampilkan Nama
A Menampilkan Alamat
K Menampilkan Kode Pos
P Menampilkan Prodi
L Menampilkan Kelas
e Menampilkan Email
k Keluar""")
def tampilkanNim():
    nim = data["NIM"]
    print("NIM : ", nim)
def tampilkanNama():
    nama = data["NAMA"]
    print("Nama : ", nama)
def tampilkanAlamat():
    univ = data["ALAMAT"]
    print("Alamat : ", univ)
def tampilkanPost():
    fakultas = data["POST"]
    print("Kode Pos : ", fakultas)
def tampilkanProdi():
    prodi = data["PRODI"]
    print("Prodi : ", prodi)
def tampilkanKelas():
    kelas = data["KELAS"]
    print("Kelas : ", kelas)
def tampilkanEmail():
    email = data["EMAIL"]
    print("Email : ", email)

# Output
print("+------------------------------+")
print("""| Untuk Menampilkan Informasi  |
| Harap Masukkan Kode Angkanya |""")
print("+------------------------------+")
print("Pilihan yang tersedia :")
print("""b Menampilkan bantuan ini
N Menampilkan NIM
a Menampilkan Nama
A Menampilkan Alamat
K Menampilkan Kode Pos
P Menampilkan Prodi
L Menampilkan Kelas
e Menampilkan Email
k Keluar""")

# Logic
while True:
    pilihan = str(input("Masukkan Pilihan Anda => "))
    if pilihan == "b":
        bantuan()
    elif pilihan == "N":
        tampilkanNim()
    elif pilihan == "a":
        tampilkanNama()
    elif pilihan == "A":
        tampilkanAlamat()
    elif pilihan == "K":
        tampilkanPost()
    elif pilihan == "P":
        tampilkanProdi()
    elif pilihan == "L":
        tampilkanKelas()
    elif pilihan == "e":
        tampilkanEmail()
    elif pilihan == "k":
        print("Selesai!")
        break
    else:
        print("Pilihan Tidak Valid!")
        break