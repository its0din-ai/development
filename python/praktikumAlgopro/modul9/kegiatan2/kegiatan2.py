# Praktikum Modul 9 - Menulis Berkas Teks
# Oleh, Muhammad Wahyu Syafi'uddin
# NIM : L200210056

f = open('../kegiatan1/L200210056', 'a+')
f.write("KLATEN")
f.seek(0)
perbaris = f.readlines()

nim = perbaris[0].strip("\n")
tanggal = perbaris[1].split("-")
tanggalBaru = str(tanggal[1] + "/" + tanggal[0] + "/" + tanggal[2].strip("\n"))
namaLengkap = perbaris[2].strip("\n")
kota = perbaris[3].strip("\n")

f.close()

print(namaLengkap)
print(f"{kota}, {tanggalBaru}")
print(nim)

