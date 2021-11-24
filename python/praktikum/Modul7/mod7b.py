# Praktikum Modul 7 Point B
# Oleh, Muhammad Wahyu Syafi'uddin
# NIM : L200210056

db_pass = "wahyu"
timeOut = 0

while timeOut < 3:
    pass_input = str(input("Masukkan Password: "))
    if pass_input == db_pass:
        print("Password Benar, Selamat Datang !")
        break
    elif timeOut == 2:
        print("Anda telah mencoba 3 kali, Akses anda ditolak !")
        break
    else:
        print("Maaf, Anda salah memasukkan Password !")
        timeOut += 1



