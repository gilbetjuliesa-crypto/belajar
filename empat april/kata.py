text = 'A quick brown fox jumps over the lazy dog.'

def ambil_kata_kalimat(kalimat, n):
    kalimat = kalimat.lower() #ubah huruf kecil
    hasil_akhir = [] #siapkan tempat hasil
    hasil = kalimat.split() #pecah berdasarkan spasi
    for i in range (0,len(hasil)): #loop per hasil pecah
        tmp = ' '.join(hasil[i:i + n]) #ambil per indeks
        hasil_akhir.append(tmp) #tambahkan ke list

    return hasil_akhir #return
print(ambil_kata_kalimat(text, 3))

