n = 4
key = ["nama_produk", "id_produk", "jumlah_produk"]
value1 = []
value2 = []
value3 = []
value = []
for i in range(1, n):
    zz = input("input iterasi ke-{i} \n".format(i=i))
    listgw = zz.split(" / ")
    for j in range(len(listgw)):
        newlist = listgw[j].split(" : ")
        values = str(newlist[1])
        if i == 1:
            value1.append(values)
        elif i == 2:
            value2.append(values)
        elif i == 3:
            value3.append(values)

kamus1 = dict(zip(key, value1))
kamus2 = dict(zip(key, value2))
kamus3 = dict(zip(key, value3))

value.append(kamus1)
value.append(kamus2)
value.append(kamus3)
print(value)