nim = {'71200120', '71200195', '71200214'}
jumlah_nim = len(nim)
print(jumlah_nim)

for n in nim:
    print(n)

bilangan_1 = {1, 2, 3, 4, 5, 6}
bilangan_2 = {6, 7, 8, 9, 10}

gabungan = bilangan_1 | bilangan_2
print(gabungan) #menggabungkan 2 variabel
print(len(gabungan)) #mengitung berapa angka dan tidak menghitung angka yang sama

irisan = bilangan_1 & bilangan_2
print(irisan) #mencari angka yang sama dari 2 variabel

x = bilangan_1 - bilangan_2
print(x) #

x2 = bilangan_2 - bilangan_1
print(x2 )

y = bilangan_1.symmetric_difference(bilangan_2)
print(y) #angka yang sama hilang 



# definisikan sebuah set kosong
plat_nomor = set()

# tambahkan plat nomor
plat_nomor.add('AB 1890 XA')
plat_nomor.add('AD 6810 MT')

# jumlah anggota di dalam set
print(len(plat_nomor))

# tambahkan plat yang sama sekali lagi
plat_nomor.add('AB 1890 XA')

# tampilkan semua plat nomor
for plat in plat_nomor:
    print(plat)

bilangan_prima = {13, 23, 7, 29, 11, 5}

# hapus 5 dari set tersebut
bilangan_prima.remove(5)
print(bilangan_prima)  # {7, 11, 13, 23, 29}

# hapus 97 (tidak ada)
bilangan_prima.discard(97)
print(bilangan_prima)  # {7, 11, 13, 23, 29}

# ambil dan hapus salah satu elemen
bilangan = bilangan_prima.pop()
print(bilangan)        # contoh: 7 (acak, bisa berbeda)
print(bilangan_prima)  # {11, 13, 23, 29}

# kosongkan set
bilangan_prima.clear()
print(bilangan_prima)  # set()

