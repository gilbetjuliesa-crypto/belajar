def findNIM(text):
    kata = text.split()
    hasil = []

    for k in kata:
        k = k.strip(".,()")

        if len(k) == 8:
            huruf = k[:2]
            angka = k[2:]

            if huruf.isalpha() and huruf.isupper() and angka.isdigit():
                hasil.append(k)

    garis = "============================================="

    print(garis)
    print("Total NIM :", len(hasil))

    if len(hasil) == 0:
        print("List NIM : Tidak ada")

    elif len(hasil) == 1:
        print("List NIM :", hasil[0])

    elif len(hasil) == 2:
        print("List NIM :", hasil[0], "and", hasil[1])

    else:
        tampil = ""
        for i in range(len(hasil)):
            if i == len(hasil) - 1:
                tampil += "and " + hasil[i]
            else:
                tampil += hasil[i] + ", "
        print("List NIM :", tampil)

    print(garis)


if __name__ == "__main__":
    stript = input()
    findNIM(stript)