# Praktikum Modul 8 - Konversi Suhu
# Oleh, Muhammad Wahyu Syafi'uddin
# NIM : L200210056

def konversiSuhu(default=0, C="A", F="a"):
    if default != 0:
        kalkulasi = default * 9/5 + 32
        print("Suhu {} Celcius Setara dengan {} Fahrenheit".format(default, kalkulasi))
    elif C != "A":
        kalkulasi = C * 9/5 + 32
        print("Suhu {} Celcius Setara dengan {} Fahrenheit".format(C, kalkulasi))
    elif F != "a":
        kalkulasi = (F - 32) * 5/9
        print("Suhu {} Fahrenheit Setara dengan {} Celcius".format(F, kalkulasi))
    else:
        x = 0
        kalkulasi = x * 9/5 + 32
        print("Suhu {} Celcius Setara dengan {} Fahrenheit".format(x, kalkulasi))

