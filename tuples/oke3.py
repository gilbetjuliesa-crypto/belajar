# input jumlah kategori (pakai eval)
n = eval(input("Masukkan jumlah kategori: "))

data_aplikasi = {}

for i in range(n):
    nama_kategori = input("Masukkan nama kategori: ")
    print("Masukkan 5 nama aplikasi di kategori", nama_kategori)
    
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input("Nama aplikasi: ")
        aplikasi.append(nama_aplikasi)
    
    data_aplikasi[nama_kategori] = aplikasi

print("\nData Aplikasi:")
print(data_aplikasi)

daftar_set = []
for aplikasi in data_aplikasi.values():
    daftar_set.append(set(aplikasi))

# 1. Aplikasi yang muncul di SEMUA kategori
hasil_intersection = daftar_set[0]
for i in range(1, len(daftar_set)):
    hasil_intersection = hasil_intersection.intersection(daftar_set[i])

print("\nAplikasi yang muncul di semua kategori:")
print(hasil_intersection)


# 2. Aplikasi yang hanya muncul di SATU kategori
semua_aplikasi = []
for s in daftar_set:
    semua_aplikasi.extend(list(s))

unik_satu = set()
for app in semua_aplikasi:
    if semua_aplikasi.count(app) == 1:
        unik_satu.add(app)

print("\nAplikasi yang hanya muncul di satu kategori:")
print(unik_satu)

# 3. Aplikasi yang muncul TEPAT DI DUA kategori (n > 2)
if n > 2:
    tepat_dua = set()
    for app in set(semua_aplikasi):
        if semua_aplikasi.count(app) == 2:
            tepat_dua.add(app)
    
    print("\nAplikasi yang muncul tepat di dua kategori:")
    print(tepat_dua)