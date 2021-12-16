# Praktikum Modul 9 - Membaca Shelve
# Oleh, Muhammad Wahyu Syafi'uddin
# NIM : L200210056

import shelve

shelve_file = shelve.open('../kegiatan3/Odin')
id = shelve_file.get('idEntity')

print(f"Student Id : {id[0]}")
print(f"Name       : {id[1]}")
print(f"Birth Date : {id[2]}")

shelve_file.close()


