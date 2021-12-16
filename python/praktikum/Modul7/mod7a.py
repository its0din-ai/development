# Praktikum Modul 7 point A
# Oleh, Muhammad Wahyu Syafi'uddin
# NIM : L200210056

dataBangun = {1: [1, "Segitiga", "L = 0.5 * a * t"],
              2: [2, "Persegi", "L = s ** 2"],
              3: [3, "Persegi Panjang", "L = p * l"],
              4: [1, "Lingkaran", "L = pi * r ** 2"],
              5: [5, "Jajaran Genjang", "L = a * t"]
              }

print("\n")

print ("{:<3}| {:<18}| {:<20}".format('No', 'Nama Bangun', 'Rumus Luas'))
print("---|-------------------|------------------")

for key, value in dataBangun.items():
    no, namaBangun, rumusLuas = value
    print ("{:<3}| {:<18}| {:<15}".format(no, namaBangun, rumusLuas))

print("\n")


