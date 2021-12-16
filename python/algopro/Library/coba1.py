import datetime
 
class Manusia3(object):
    """membuat kelas manusia"""
    def __init__(self, nama, tanggal):
        self.nama = nama
        self.lahir = tanggal
 
    def tahun_lahir(self):
        """mengembalikan tahun lahir"""
        return int(self.lahir[:4])
 
    def umur(self):
        """mengembalikan umur"""
        tahun_ini = datetime.date.today().year
        return tahun_ini - self.tahun_lahir()
 
def seumur(manusia1, manusia2):
    if manusia1.lahir == manusia2.lahir:
        return "Benar"
    else:
        return "Salah"

ib = Manusia3('Ibnu Sina', '2002-11-05')
print(ib.lahir())
print(ib.tahun_lahir())
um = ib.umur()
print(um)