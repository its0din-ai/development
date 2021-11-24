# Praktikum Modul 7 Point B
# Oleh, Muhammad Wahyu Syafi'uddin
# NIM : L200210056

nama = str(input("Masukkan nama: "))
inputJam = str(input("Pukul Berapa Sekarang? "))
jam = inputJam.split(".")
pukul = list(map(int, jam))

if pukul[0] >= 5 and pukul[0] <= 10:
    print("Selamat Pagi,", nama)

elif pukul[0] >= 11 and pukul[0] <= 14:
    print("Selamat Siang,", nama)

elif pukul[0] >= 15 and pukul[0] <= 18:
    print("Selamat Sore,", nama)

else:
    print("Selamat Malam,", nama)



