def Giokstore(Member : bool, Harga_barang : int, Jenis_kemasan : str, Metode_Pembayaran : str):
    
    harga = Harga_barang

    # DISKON
    if Member:
        if Harga_barang > 500000:
            harga -= Harga_barang * 0.5
        elif 250000 <= Harga_barang <= 500000:
            harga -= Harga_barang * 0.35
        elif 100000 <= Harga_barang <= 249999:
            harga -= Harga_barang * 0.15
    else:
        if Harga_barang > 750000:
            harga -= Harga_barang * 0.5
        elif 350000 <= Harga_barang <= 750000:  
            harga -= Harga_barang * 0.35
        elif 150000 <= Harga_barang <= 349999:
            harga -= Harga_barang * 0.15

    # KEMASAN
    if Jenis_kemasan == "Plastik":
        harga += 17500
    elif Jenis_kemasan == "Kardus":
        harga += 30000

    # PEMBAYARAN
    if Metode_Pembayaran == "Cash":
        pass
    elif Metode_Pembayaran == "Kredit / QRIS":
        if Member:
            harga += harga * 0.02
        else:
            harga += harga * 0.05
    elif Metode_Pembayaran == "Kasbon":
        return "Maaf Toko ini tidak menerima pinjaman"

    return int(harga)


# #Bagian ini jangan dirubah
if __name__ == "__main__":
    member_str = input()
    member = True if member_str == "True" else False
    harga = int(input())
    kemasan = str(input())
    metode = str(input())
    print(Giokstore(member,harga,kemasan,metode))