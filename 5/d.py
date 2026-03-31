def makedecision(nama_mobil, pajak_mobil, cuci_mobil):
    
    # DATA MOBIL
    data = {
        "Innova": [450000000, 12, 500000],
        "Fortuner": [750000000, 10, 600000],
        "Hilux": [500000000, 10, 400000],
        "Navara": [600000000, 8, 1000000],
        "Terra": [800000000, 8, 500000],
        "Pajero": [600000000, 9, 700000],
        "Triton": [450000000, 9, 300000],
        "Tank 300": [980000000, 11, 950000]
    }

    # VALIDASI
    if nama_mobil not in data:
        print("Mobil apa nihh")
        return

    # AMBIL DATA
    harga_mobil = data[nama_mobil][0]
    konsumsi = data[nama_mobil][1]
    servis_500km = data[nama_mobil][2]

    # HITUNG BENSIN (1000 km)
    liter = 1000 / konsumsi
    harga_bensin = int(liter * 18500)

    # HITUNG SERVIS (1000 km = 2x servis)
    total_servis = servis_500km * 2

    # HITUNG CUCI
    total_cuci = cuci_mobil * 250000

    # TOTAL SEMUA
    total = harga_mobil + harga_bensin + total_servis + total_cuci + pajak_mobil

    # OUTPUT
    print("Daftar List Kebutuhan")
    print("Nama Mobil : ", nama_mobil)
    print("Harga Mobil : ", harga_mobil)
    print("Total Harga Bensin Mobil : ", harga_bensin)
    print("Total Servis Mobil : ", total_servis)
    print("Total Cuci Mobil : ", total_cuci)
    print("Total Daftar Kebutuhan : ", total)


#Jangan diubah
if __name__ == "__main__":
    nama = str(input())
    pajak = int(input())
    cuci = int(input())
    makedecision(nama,pajak,cuci)