kalimat = input("Masukkan kalimat: ")
kata_dicari = input("Masukkan kata yang dicari: ")

kalimat = kalimat.lower()
kata_dicari = kata_dicari.lower()

kalimat = kalimat.replace(".", "")

daftar_kata = kalimat.split()

jumlah = 0
for kata in daftar_kata:
    if kata == kata_dicari:
        jumlah += 1

print(kata_dicari, "ada", jumlah, "buah")