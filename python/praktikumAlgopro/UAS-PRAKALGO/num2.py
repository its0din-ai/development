def celcius(value):
    konversi = (value - 32) * 5/9
    print(f"{value} Fahrenheit = {konversi} Celcius")
    return("---------------------------------\n")

def fahrenheit(value):
    konversi = (value * 9/5 + 32)
    print(f"{value} Celcius = {konversi} Fahrenheit")
    return("---------------------------------\n")

options = """h = To Show the available options
1 = Convertion from Fahrenheit to Celcius (F ==> C)
2 = Convertion from Celcius to Fahrenheit (C ==> F)
k = exit
    """
print(options)
while True:
    pilihan = str(input("Your Option : "))
    if pilihan == "1":
        value = int(input("Enter Number for Conversion : "))
        print(celcius(value))
    elif pilihan == "2":
        value = int(input("Enter Number for Conversion : "))
        print(fahrenheit(value))
    elif pilihan == "h":
        print(options)
    elif pilihan == "k":
        break