# Praktikum Modul 7 Bonus
# Oleh, Muhammad Wahyu Syafi'uddin
# NIM : L200210056

# Kelas untuk menampilkan warna
class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Statement
data = {"NIM":"L200210056",
        "NAMA":"MUHAMMAD WAHYU SYAFI'UDDIN",
        "UNIVERSITAS":"UNIVERSITAS MUHAMMADIYAH SURAKARTA",
        "FAKULTAS":"FAKULTAS KOMUNIKASI DAN INFORMATIKA",
        "PRODI":"TEKNIK INFORMATIKA",
        "KELAS":"PRAKTIKUM ALGOPRO B",
        "EMAIL":"l200210056@student.ums.ac.id"
        }

# Function / Module
def tampilkanNim():
    nim = data["NIM"]
    print(f"{bcolors.OKGREEN}NIM : ", nim + f"{bcolors.ENDC}")
def tampilkanNama():
    nama = data["NAMA"]
    print(f"{bcolors.OKGREEN}Nama : ", nama + f"{bcolors.ENDC}")
def tampilkanUniversitas():
    univ = data["UNIVERSITAS"]
    print(f"{bcolors.OKGREEN}Universitas : ", univ + f"{bcolors.ENDC}")
def tampilkanFakultas():
    fakultas = data["FAKULTAS"]
    print(f"{bcolors.OKGREEN}Fakultas : ", fakultas + f"{bcolors.ENDC}")
def tampilkanProdi():
    prodi = data["PRODI"]
    print(f"{bcolors.OKGREEN}Prodi : ", prodi + f"{bcolors.ENDC}")
def tampilkanKelas():
    kelas = data["KELAS"]
    print(f"{bcolors.OKGREEN}Kelas : ", kelas + f"{bcolors.ENDC}")
def tampilkanEmail():
    email = data["EMAIL"]
    print(f"{bcolors.OKGREEN}Email : ", email + f"{bcolors.ENDC}")

# Output
print("+------------------------------+")
print("""| Untuk Menampilkan Informasi |
| Harap Masukkan Kode Angkanya |""")
print("+------------------------------+")
print("Pilihan yang tersedia :")
print("""[1] Tampilkan NIM
[2] Tampilkan NAMA
[3] Tampilkan Universitas
[4] Tampilkan Fakultas
[5] Tampilkan Prodi
[6] Tampilkan Kelas
[7] Tampilkan Email
[8] Keluar""")

# Logic
while True:
    pilihan = str(input("Masukkan Pilihan Anda => "))
    if pilihan == "1":
        tampilkanNim()
    elif pilihan == "2":
        tampilkanNama()
    elif pilihan == "3":
        tampilkanUniversitas()
    elif pilihan == "4":
        tampilkanFakultas()
    elif pilihan == "5":
        tampilkanProdi()
    elif pilihan == "6":
        tampilkanKelas()
    elif pilihan == "7":
        tampilkanEmail()
    elif pilihan == "8":
        print(f"{bcolors.OKCYAN}Terima Kasih!{bcolors.ENDC}")
        break
    else:
        print(f"{bcolors.FAIL}Maaf, Pilihan Tidak Ada!{bcolors.ENDC}")
        break