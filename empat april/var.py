def findPhoneNumber(text):
    kata = text.split()
    hasil = []

    for k in kata:
        k = k.strip(".,()")

        if "-" in k:
            cek = k.replace("-", "")

            if cek.isdigit() and len(cek) == 12 and cek.startswith("08"):
                hasil.append(k)

    garis = "============================================="

    print(garis)
    print("Total Phone :", len(hasil))

    if len(hasil) == 0:
        print("List Phone : Nomor is not define")

    elif len(hasil) == 1:
        print("List Phone :", hasil[0])

    elif len(hasil) == 2:
        print("List Phone :", hasil[0], "and", hasil[1])

    else:
        tampil = ""
        for i in range(len(hasil)):
            if i == len(hasil) - 1:
                tampil += "and " + hasil[i]
            else:
                tampil += hasil[i] + ", "
        print("List Phone :", tampil)

    print(garis)


if __name__ == "__main__":
    text = input()
    findPhoneNumber(text)