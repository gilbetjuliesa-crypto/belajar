def nilai_kata(kalimat, kata_cari):
    kalimat = kalimat.lower().split()
    kata_cari = kata_cari.lower().split()

    total = 0

    for kata in kata_cari:
        if kata in kalimat:
            total += len(kata)

    if len(kata_cari) % 2 == 0:
        total *= 2

    print("Total Nilai :", total)

# contoh
nilai_kata("saya suka makan nasi", "makan nasi")