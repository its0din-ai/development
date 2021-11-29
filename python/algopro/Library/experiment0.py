import random
import string

def captha1():
    opr = ["+", "-"]
    num2 = int(random.choice(range(0, 100)))
    num1 = int(random.choice(range(num2, 200)))
    op = random.choice(opr)
    if op == '+':
        c = num1, op, num2
        print("Jawablah Hasil Dari :")
        print(' '.join(map(str, c)))
        a = int(input("=> "))
        if a == num1 + num2:
            print("Benar")
        else:
            print("Salah")
    elif op == '-':
        c = num1, op, num2
        print("Jawablah Hasil Dari :")
        print(' '.join(map(str, c)))
        a = int(input("=> "))
        if a == num1 - num2:
            print("Benar")
        else:
            print("Salah")
    else:
        print('Error')

def captha2():
    chars = string.ascii_uppercase + string.digits
    key = ''.join(random.choice(chars) for _ in range(5))
    print("Untuk Melanjutkan, silahkan menulis kode yang ada")
    print("Kode :", key)
    a = input("*Case Insensitive* => ")
    if a.upper() == key:
        print("Benar")
    else:
        print("Salah")

print("Program Captcha")
print("[1] Captcha Hitungan")
print("[2] Captcha Kode")
ver = int(input("Masukkan Versi Captcha => "))
if ver == 1:
    captha1()
elif ver == 2:
    captha2()
else:
    print("Versi Tidak Ditemukan")
