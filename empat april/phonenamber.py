def findPhoneNumber(text):
    kata2 = text.split()
    nomor = []

    for k in kata2:
        k = k.strip(".,()")

        if "-" in k:
            angka = k.replace("-", "")

            if angka.isdigit() and len(angka) == 12:
                nomor.append(k)

    print("==========================================")
    print("Total Phone Number Prof Wisnu :", len(nomor))

    if not nomor:
        print("List Phone Number : Nomor is not define")
    else:
        hasil = ""

        for i in range(len(nomor)):
            if i == len(nomor) - 1 and len(nomor) > 1:
                hasil += "and " + nomor[i]
            elif i == len(nomor) - 2:
                hasil += nomor[i] + " "
            else:
                hasil += nomor[i]
                if len(nomor) > 2:
                    hasil += ", "

        print("List Phone Number :", hasil)

    print("==========================================")


if __name__ == "__main__":
    text = input()
    findPhoneNumber(text)