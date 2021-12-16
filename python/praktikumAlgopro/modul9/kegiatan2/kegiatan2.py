f = open('L200210056', 'a+')
f.write('\n')
f.write('Indonesia')
f.seek(0)
perbaris = f.readlines()

tanggal = perbaris[1].split("-")
tanggalBaru = str(tanggal[1] + "/" + tanggal[0] + "/" + tanggal[2])



f.close()
print(perbaris)
print(tanggalBaru)