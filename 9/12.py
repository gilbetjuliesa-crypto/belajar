def hapus_spasi(kalimat):
    return " ".join(kalimat.split())

# input
kalimat = input("Masukkan kalimat: ")
print("Hasil:", hapus_spasi(kalimat))