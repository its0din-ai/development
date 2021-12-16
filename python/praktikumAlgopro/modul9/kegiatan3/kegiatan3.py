# Praktikum Modul 9 - Menulis Berkas Teks
# Oleh, Muhammad Wahyu Syafi'uddin
# NIM : L200210056

import shelve

f = open('../kegiatan1/L200210056', 'r')
dataF = f.readlines()

nim = str(dataF[0].strip())
nama = str(dataF[2].strip())
tanggalLahir = str(dataF[1].strip())

almariData = shelve.open('Odin')
almariData["idEntity"] = [nim, nama, tanggalLahir]
almariData.close()