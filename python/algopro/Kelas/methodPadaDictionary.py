#Membuat dictionary mhs1 dengan pasangan key-value 
mhs1 = {'Name': 'Susan', 'Age': 17, 'Semester': 1}
 
#Mencetak value dari key Name pada dictionary mhs1
print(mhs1.get('Name'))
print(mhs1['Name'])
 
#Mencetak pasangan key-value yang ada pada dictionary mhs1
print(mhs1.items())
 
#Mencetak key yang ada pada dictionary mhs1
print(mhs1.keys())
 
#Mencetak value yang ada pada dictionary mhs1
print(mhs1.values())
 
#Mencetak value pada key Age menjadi 18 untuk mhs1
mhs1.update({"Age":18})
 
#Mencetak dictionary mhs1
print(mhs1)
 
#Menghapus dan mengambil value dari key Age pada dictionary mhs1, kemudian mencetak nilainya
pop_age = mhs1.pop('Age')
print(pop_age)
 
#Menghapus dan mengambil pasangan key-value terakhir pada dictionary mhs1, kemudian mencetak nilainya
pop_itm = mhs1.popitem()
print(pop_itm)
 
#Mencetak dictionary mhs1
print(mhs1)