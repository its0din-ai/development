def tinggi(angka):
    listAngka = angka.split(',')
    for i in range(0, len(listAngka)):
        listAngka[i] = int(listAngka[i])
    
    mx = max(listAngka)
    print(mx)

"""
fungsi mengambil argumen dari parameter
value di hapus dari karakter koma
melakukan perulangan untuk konversi List yang berisi string menjadi integer
mencari nilai tertinggi dari List dengan method Max
menampilkan nilai tertinggi
"""

