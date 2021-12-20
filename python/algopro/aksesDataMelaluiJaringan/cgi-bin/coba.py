#!/usr/bin/env python3
import datetime
 
def hitung_umur(lahir):
    "menentukan umur sejak tanggal lahir tertentu"
    hari_ini = datetime.date.today()
    tahun = hari_ini.year - lahir.year
    bulan = hari_ini.month - lahir.month
    if bulan < 0:
        tahun -= 1
        bulan += 12
    return tahun, bulan
 
lahir = datetime.date(1999, 2, 15) # lahir 20 September 2000
thn, bln = hitung_umur(lahir)
nama = "Wahyu"  # ganti dengan nama panggilan Anda
 
htm = f"""<!DOCTYPE html>
 
<html>
<head>
<title>Server dengan konten dinamis</title>
</head>
<body>
<p>{nama} lahir pada tanggal {lahir}.</p>
<p>Hari ini adalah tanggal {datetime.date.today()}.</p>
<p>Karena itu Doni berumur {thn} tahun {bln} bulan.</p>
<p>Terima kasih</p>
</body>
</html>"""
 
print(htm)