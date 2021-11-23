# Menghitung Harga Bensin

class kalkulasi:
    hargaBensin = {"Pertalite" : 7500, "Pertamax" : 9000, "Pertamax-Turbo" : 12000}
    def __init__(self,vol, harga=hargaBensin):
        self.vol = vol
        self.lite = harga["Pertalite"]
        self.max = harga["Pertamax"]
        self.turbo = harga["Pertamax-Turbo"]
    
    def pertalite(self):
        return self.vol * self.lite
    def pertamax(self):
        return self.vol * self.max
    def pertamaxTurbo(self):
        return self.vol * self.turbo

print("Beli Bensin Gan?")
varian = input("Beli Bensin mana Bang? Saran Gue Pertamax Turbo, biar makin kentjeng\n[1] Pertalite\n[2] Pertamax\n[3] Pertamax Turbo\n==> ")
if varian.lower() == "pertalite" or "1" or "a":
    vol = int(input("Mau beli Berapa? ", "Liter"))
    hasill = kalkulasi(vol)
    print("Oke, total harga Rp {:,}". format(hasill.pertalite()),"Bang")
elif varian.lower() == "pertamax":
    vol = int(input("Mau beli Berapa Liter : "))
    hasilp = kalkulasi(vol)
    print("Oke, total harga Rp {:,}". format(hasilp.pertamax()),"Bang")
elif varian.lower() == "pertamax turbo" or "pertamaxturbo":
    vol = int(input("Mau beli Berapa Liter : "))
    hasilt = kalkulasi(vol)
    print("Oke, total harga Rp {:,}". format(hasilt.pertamaxTurbo()),"Bang")