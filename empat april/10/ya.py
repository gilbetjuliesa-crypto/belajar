z = input('Masukkan nama file sertakan format file\t: ')
y = input('Masukkan nama file sertakan format file\t: ')
test1 = open(z, 'r')
with open(z,'r+') as test1, open(y,'r+') as test2:
    a = test1.readlines()
    b = test2.readlines()
    if a == b:
        print ("File Sama")
    else:
        c = len(a)
        d = len(b)
        if c == d:
            for i in range (0,c):
                baris1 = a[i]
                baris2 = b[i]
                if a[i] == b[i]:
                    print (f"Baris ke {i+1} sama\n")
                else:
                    print (f"Baris ke {i+1} beda")
                    print (f"Teks 1 :\n{a[i].strip()}")
                    print (f"Teks 2 :\n{b[i].strip()}\n")