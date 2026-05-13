nama = eval(input("Masukkan nama: "))

lst = list()

for item in nama:
    lst.append((len(item), item))

lst.sort(reverse=True)

hasil = list()

for panjang, item in lst:
    hasil.append(item)

print(tuple(hasil))