# Praktikum Modul 7 Point B
# Oleh, Muhammad Wahyu Syafi'uddin
# NIM : L200210056

from time import localtime, strftime
import time

print("\nProgram Menampilkan Waktu Komputer:")
while True:
    waktu = strftime("%H:%M:%S", localtime())
    detik = strftime(":%S", localtime())
    print(waktu)
    time.sleep(1)

    if detik == ":00":
        print("Jam Praktikum Sudah Habis, Silahkan Pulang !\n")
        break


