# Memfilter bilangan genap kelipatan 3
# dan mengurutkan hasilnya

nilai = [37, 99, 48, 55, 12, 20, 90, 47, 21, 30, 80]
genap_kelipatan_3 = []

for i in nilai:
    if i % 3 == 0:
        genap_kelipatan_3.append(i)
        genap_kelipatan_3.sort()

print(genap_kelipatan_3)