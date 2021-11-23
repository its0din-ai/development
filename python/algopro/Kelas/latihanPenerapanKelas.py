class Mobil():
    'membuat kelas mobil'
    warna = 'biru'
    harga = 100000000
    posisi = (106, -5)

    def bergerak(self, koordinat):
        'merubah posisi mobil'
        self.posisi = koordinat


a = Mobil()  # membuat objek
print(a.warna)
a.bergerak((100, -3))
print(a.posisi)