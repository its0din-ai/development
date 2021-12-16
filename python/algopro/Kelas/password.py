import hashlib

db_pass = "7b24afc8bc80e548d66c4e7ff72171c5" # toor
pass_input = str(input("Masukkan Password: "))
crypt = hashlib.md5(pass_input.encode())
crypted = crypt.hexdigest()
to = 2

while to > 0:
    if crypted == db_pass:
        print("Password Benar")
        break
    else:
        print("Password Salah")
        to -= 1
        pass_input = str(input("Masukkan Password: "))
        if to == 0:
            print("Anda telah mencoba 3x, Akses anda dibatasi!")