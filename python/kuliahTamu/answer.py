def fungsi(n):
    jum = 0
    kali = 1

    while n> 0:
        mod = n % 10
        jum = jum + mod
        kali = kali * mod
        n = n // 10
    return jum, kali

z = int(input("Min => "))
y = int(input("Maks => "))
x = y+1

for i in range(z,x):
    jum, kali = fungsi(i)
    if jum == kali:
        print(i)