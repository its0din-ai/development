class Manusia(object):
    """ membuat kelas manusia """
    lahir = '2000-04-20'
 
    def tahun_lahir(self):
        """mengembalikan tahun lahir"""
        th = self.lahir[:4]
        return int(th)
 
budi = Manusia()
print(budi.lahir)
budi.lahir = '2004-09-14'
print(budi.tahun_lahir())