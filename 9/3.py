kalimat = input("Masukkan kalimat: ")

hasil = ""
spasi = False

for i in range(len(kalimat)):
    if kalimat[i] != " ":
        hasil += kalimat[i]
        spasi = False
    else:
        if not spasi:
            hasil += " "
            spasi = True

hasil = hasil.strip()

print("Hasil:", hasil)