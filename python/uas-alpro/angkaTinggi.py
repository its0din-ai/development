def tinggi(tanyaTinggi):
    hapusDelim = tanyaTinggi.split(',')
    for i in range(0, len(hapusDelim)):
        hapusDelim[i] = int(hapusDelim[i])
    
    maksimum = max(hapusDelim)
    print(maksimum)

"""
fungsi mengambil argumen dari parameter
value di hapus dari karakter koma
melakukan perulangan untuk konversi List yang berisi string menjadi integer
mencari nilai tertinggi dari List dengan method Max
menampilkan nilai tertinggi
"""

