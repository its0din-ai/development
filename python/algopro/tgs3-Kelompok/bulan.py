
kalimat=['aku lahir pada bulan 1', 'liburan di bulan desember ini akan sangat menyenangkan']
# fileTeks = open("berangka.txt", "r")
# kalimat = fileTeks.readlines()
# fileTeks.close()
bulan=['januari','februari','maret','april','mei','juni','juli','agustus','september','oktober','november','desember']
for i in range(len(kalimat)):
    
    for j in range(len(bulan)):
        if bulan[j] in kalimat[i].lower():
            print(f"ketemu, ada di indeks ke {i}")
            print(f"Pada kalimat => {kalimat[i]}")