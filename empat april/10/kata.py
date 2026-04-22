def kata_terpanjang(nama_file):
    try:
        with open(nama_file) as f:
            max_kata = ""
            
            for line in f:
                words = line.split()
                for w in words:
                    if len(w) > len(max_kata):
                        max_kata = w

        print("Kata terpanjang:", max_kata)
        print("Panjang:", len(max_kata))

    except:
        print("File Tidak Ada Prof")


if __name__ == "__main__":
    nama = input()
    kata_terpanjang(nama)