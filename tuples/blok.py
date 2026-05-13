def hitung_total_belanja(data):

    if data == []:
        return "Gak Niat Belanja Ta?"

    barang = {}
    hasil = []

    for nama, jumlah, harga in data:

        total = jumlah * harga

        if nama in barang:
            barang[nama] = barang[nama] + total
        else:
            barang[nama] = total

    for nama in barang:
        hasil.append((nama, barang[nama]))

    hasil.sort(key=lambda x: x[1], reverse=True)

    return tuple(hasil)



data_belanja = eval(input("Masukkan data belanja: "))

print("Hasil Prof :", hitung_total_belanja(data_belanja))