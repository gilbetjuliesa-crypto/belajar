def jumlah_ganjil(n, i=1):
    if (2 * i - 1) > n:
        return 0

    return (2 * i - 1) + jumlah_ganjil(n, i + 1)

angka = int(input("Masukkan batas bilangan ganjil: "))

hasil = jumlah_ganjil(angka)
print("Jumlah deret ganjil =", hasil)