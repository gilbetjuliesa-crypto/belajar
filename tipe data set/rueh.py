def palindrom(teks):
    if len(teks) == 0 or len(teks) == 1:
        return True
    
    if teks[0] != teks[len(teks) - 1]:
        return False
    return palindrom(teks[1:len(teks) - 1])

kalimat = input("Masukkan kalimat: ")
kalimat = kalimat.lower().replace(" ", "")

if palindrom(kalimat):
    print("Kalimat tersebut adalah PALINDROM")
else:
    print("Kalimat tersebut BUKAN PALINDROM")