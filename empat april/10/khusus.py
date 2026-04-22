import re

def hitung(nama_file):
    try:
        with open(nama_file) as f:
            gabriel = 0
            vie = 0
            baris_khusus = 0

            for line in f:
                w = len(re.findall('gabriel', line))
                p = len(re.findall('vie', line))

                gabriel += w
                vie += p

                if w > 0 or p > 0:
                    baris_khusus += 1

        print("gabriel:", gabriel)
        print("vie:", vie)
        print("Baris khusus:", baris_khusus)

    except:
        print("File Tidak Ada Prof")


if __name__ == "__main__":
    nama = input()
    hitung(nama)