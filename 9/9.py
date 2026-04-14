def hitung_kata(kalimat, kata_dicari):
    kalimat = kalimat.lower().replace(".", "")
    kata_dicari = kata_dicari.lower()
    
    kata_list = kalimat.split()
    
    jumlah = 0
    for kata in kata_list:
        if kata == kata_dicari:
            jumlah += 1
    
    return jumlah

# input
kalimat = input("Kalimat: ")
kata = input("Kata dicari: ")

print(kata, "ada", hitung_kata(kalimat, kata), "buah")