n = int(input("Masukkan jumlah kategori: "))

kategori = []


for i in range(n):
    data = input(f"Masukkan nama aplikasi kategori ke-{i+1} (format set, contoh: {'A','B'}): ")
    kategori.append(eval(data)) 

semua = set().union(*kategori)

unik = set()

dua = set()

for app in semua:
    jumlah = 0
    for k in kategori:
        if app in k:
            jumlah += 1
    
    if jumlah == 1:
        unik.add(app)
    elif jumlah == 2:
        dua.add(app)

# output
print("Aplikasi hanya di 1 kategori:", unik)
print("Aplikasi tepat di 2 kategori:", dua)