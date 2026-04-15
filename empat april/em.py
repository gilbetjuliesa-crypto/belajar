def findEmail(text):
    kata = text.split()
    hasil = []

    for k in kata:
        k = k.strip(".,()")

        if "@" in k and k.endswith(".com"):
            bagian = k.split("@")
            if len(bagian) == 2:
                nama = bagian[0]
                domain = bagian[1].replace(".com", "")

                if nama.isalnum() and domain.isalnum():
                    hasil.append(k)

    garis = "============================================="

    print(garis)
    print("Total Email :", len(hasil))

    if len(hasil) == 0:
        print("List Email : Email is not define")

    elif len(hasil) == 1:
        print("List Email :", hasil[0])

    elif len(hasil) == 2:
        print("List Email :", hasil[0], "and", hasil[1])

    else:
        tampil = ""
        for i in range(len(hasil)):
            if i == len(hasil) - 1:
                tampil += "and " + hasil[i]
            else:
                tampil += hasil[i] + ", "
        print("List Email :", tampil)

    print(garis)


if __name__ == "__main__":
    text = input()
    findEmail(text)