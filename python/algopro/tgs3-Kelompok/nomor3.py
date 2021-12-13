def cekAngka(inputString):

    """ Membuat String kosong bernama akhir """
    akhir = ""

    """
    Perulangan untuk cek angka dengan method isdigit
    Jika ada angka, maka akan dimasukkan ke string akhir

    """
    for char in inputString:
        if char.isdigit():
            akhir += char
    
    """
    dengan method any() akan memeriksa apakah
    string akhir kosong atau isi, jika isi akan
    mengembalikan True, dan sebaliknya

    Dan jika true, akan mencetak angka 1,
    dan jika false, akan mencetak angka 0
    
    """
    hasil = any(akhir)
    if hasil == True:
        print(akhir)
        print(1)
    else:
        print(akhir)
        print(0)


cekAngka("1 Aku mendapatkan nilai 54521")       # bernilai 1, karena ada angka
cekAngka("Aku mendapatkan nilai seratus")   # bernilai 0, karena tidak ada angka