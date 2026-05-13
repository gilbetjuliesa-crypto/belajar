data = eval(input("Masukkan data: "))

print("Data :", data)

nama, nim, alamat = data

print("NIM :", nim)
print("NAMA :", nama)
print("ALAMAT :", alamat)

tuple_nim = tuple(nim)
print("NIM :", tuple_nim)

nama_depan = tuple(nama.split()[0][1:])
print("NAMA DEPAN :", nama_depan)

nama_terbalik = tuple(nama.split()[::-1])
print("NAMA TERBALIK :", nama_terbalik)