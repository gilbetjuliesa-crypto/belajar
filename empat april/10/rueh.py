a = open("Test3.txt","r")
b = a.readlines()
nilai = 0
for i in range (len(b)):
    print ()
    temp = b[i].strip().split("||")
    soal = temp[0].capitalize().strip()
    jawab = temp[1].lower().strip()
    print (soal)
    jawab1 = input("\nSilahkan masukan jawaban anda\n>> ").lower().strip()
    if jawab1 == jawab:
        print ("Jawaban anda benar")
        nilai += 20
    else:
        print ("Jawaban anda salah")
print (f"\nNilai anda {nilai}")