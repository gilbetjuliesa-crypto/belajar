def hitung_nilai_kata(list_kata, list_cari):
    list_kata = list_kata.lower().split()
    list_cari = list_cari.lower().split()

    total = 0

    for kata in list_cari:
        jumlah = list_kata.count(kata)
        total += jumlah * len(kata)

    if len(list_cari) % 2 == 0:
        total *= 3

    print("Total Count Nilai :", total)