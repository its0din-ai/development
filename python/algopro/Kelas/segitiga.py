# class Segitiga:
#    alas = 1
#    tinggi = 2
#
# segitiga1 = Segitiga()
# segitiga2 = Segitiga()
#
# print("Alas segitiga 1 : ", segitiga1.alas)
# print("Tinggi segitiga 1 : ", segitiga1.tinggi)
# print("Alas segitiga 2 : ", segitiga2.alas)
# print("Tinggi segitiga 2 : ", segitiga2.tinggi)

class Segitiga:
    def __init__(self, alas=1, tinggi=1, sisi=1.118):
        self.alas = alas
        self.tinggi = tinggi
        self.sisi = sisi

    def hitungLuas(self):
        return 0.5 * self.alas * self.tinggi

    def hitungKeliling(self):
        return self.sisi + self.sisi + self.sisi


segitiga1 = Segitiga(20, 10)
print("Alas segitiga 1 : ", segitiga1.alas)
print("Tinggi segitiga 1 : ", segitiga1.tinggi)
print("Luas segitiga 1 : ", segitiga1.hitungLuas())
print("Keliling Segitiga 1: ", segitiga1.hitungKeliling())
print("\n")
segitiga2 = Segitiga(3, 5)
print("Alas segitiga 2 : ", segitiga2.alas)
print("Tinggi segitiga 2 : ", segitiga2.tinggi)
print("Luas segitiga 2 : ", segitiga1.hitungLuas())
print("Keliling Segitiga 2: ", segitiga1.hitungKeliling())
