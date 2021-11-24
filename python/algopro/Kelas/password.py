db_pass = "admin123"

pass_input = str(input("Masukkan password: "))
to = 2
while to > 0:
    if pass_input == db_pass:
        print("Password benar")
        break
    else:
        print("Password salah")
        to -= 1
        pass_input = str(input("Masukkan password: "))
        if to == 0:
            print("Anda telah mencoba 3x, akun anda di blokir")