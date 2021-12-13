import time
rd1 = open("berangka.txt", "r")
brs = rd1.readlines()
rd1.close()

karakter = brs
hasil = []
krk = str(karakter)
for i in range(len(karakter)):
    for ch in karakter[i]:
        if ch.isdigit():
            hasil += [karakter[i]]
            break

jumlah = len(hasil)
print(f"Ada {jumlah} Kalimat yang mengandung angka di file berangka.txt, dan sudah dimasukkan ke file hasil.txt")
print("Sedang menulis File...")
time.sleep(3)
print("Selesai!")

textfile = open("hasil.txt", "w")
for element in hasil:
    textfile.write(element)
textfile.close()
