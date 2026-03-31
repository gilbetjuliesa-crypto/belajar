def HitungBiayaImpor(harga, kondisi, jenis, negara):
    if kondisi == "Bekas":
        return harga * 0.5
    
    elif kondisi == "Baru":
        if jenis == "EV":
            return 0
        else:  
            if negara == "Indonesia":
                return harga * 0.5
            elif negara == "Malaysia":
                return harga * 0.6
            elif negara == "Jepang":
                return harga * 0.7
            elif negara == "Jerman":
                return harga * 0.85
            elif negara == "Amerika":
                return harga * 0.9


if __name__ == "__main__":
    harga = int(input()) 
    kondisi = input() 
    jenis = input() 
    negara = input()
    
    hasil = HitungBiayaImpor(harga, kondisi, jenis, negara)
    print(int(hasil))