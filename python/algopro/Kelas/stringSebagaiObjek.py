# Membuat object dari class str
kata = "Hello world"

# Menampilkan nilai object
print("kata = " + kata)

# Mengkonversi nilai string object menjadi uppercase dengan method upper
print("kata uppercase = " + kata.upper())

# Mengkonversi string menjadi lowercase dengan method lower (tanpa melalui referensi objek)
print("kata lowercase = " + "Hello world".lower())

# Mengkonversi huruf pertama pada tiap kata pada nilai object dengan method capitalize
print("kata capitalize = " + kata.capitalize())

# Mengembalikan nilai True apabila string adalah alphabet
print("Apakah kata berupa alphabet = " + str(kata.isalpha()))

# Mengembalikan nilai True apabila string adalah numeric / digit
print("Apakah kata berupa digit = " + str(kata.isdigit()))

# Mengembalikan nilai True apabila string adalah alphabet atau numeric / digit
print("Apakah kata berupa alphanumeric = " + str(kata.isalnum()))

# Mengembalikan nilai True apabila string tersempan dalam uppercase
print("Apakah kata tertulis dalam uppercase = " + str(kata.isupper()))

# Mengembalikan nilai True apabila string tersempan dalam lowercase
print("Apakah kata tertulis dalam lowercase = " + str(kata.islower()))

# Mengembalikan sebuah list yang menyimpan item dari string, yang dipisahkan oleh whitespace
print(kata.split())

# Mengembalikan sebuah list yang menyimpan item dari string, yang dipisahkan oleh karakter "l"
print(kata.split("w"))

# Mengembalikan sebuah string yang berupa gabungan semua item dari string kata, bersama dengan karakter "-" diantara setiap itemnya
print("-".join(kata))