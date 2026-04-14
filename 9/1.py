kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

kata1 = kata1.lower()
kata2 = kata2.lower()


if len(kata1) != len(kata2):
    print("Bukan anagram")
else:
    cocok = True

    for huruf in kata1:
        if kata1.count(huruf) != kata2.count(huruf):
            cocok = False
            break

    if cocok:
        print("Anagram")
    else:
        print("Bukan anagram")