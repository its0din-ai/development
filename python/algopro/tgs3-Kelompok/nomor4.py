
# Membaca file per baris, dan dimasukkan kedalam List
fileTeks = open("berangka.txt", "r")
kalimat = fileTeks.readlines()
fileTeks.close()

hasil = []
# Perulangan untuk cek setiap List apakah terdapat angka
for i in range(len(kalimat)):
    for char in kalimat[i]:
        if char.isdigit():
            # Setiap Index yang memiliki angka akan ditambahkan ke List Hasil
            hasil += [kalimat[i]]
            break

# Hanya untuk menampilkan informasi angka di Console
jumlah = len(hasil)
jml = len(kalimat)
# print(f"Ada {jumlah} Kalimat yang mengandung angka di file berangka.txt, dan sudah dimasukkan ke file hasil.txt")
print(f"Ada {jumlah}/{jml} Kalimat Mengandung angka di file berangka.txt, dan sudah dimasukkan ke file hasil.txt")

# Menulis File hasil.txt dengan isi dari List Hasil
hasilAkhir = open("hasil.txt", "w")
for kalimatAngka in hasil:
    hasilAkhir.write(kalimatAngka)
hasilAkhir.close()