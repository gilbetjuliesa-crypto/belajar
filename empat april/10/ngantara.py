a = input("Silahkan masukan judul yang dicari\n>> ").lower()
with open('daftarbuku.txt') as teks1:
    list1 = []
    for line in teks1:
        list1.append(line)
    for i in range (0,len(list1)):
        temp = list1[i].split(",")
        for i in range (0,len(temp)):
            temp1 = temp[i].lower().strip()
            if a == temp1:
                print (f"Buku Ditemukan!\n")
                print (f"Nama\t\t: {temp[0].strip()}")
                print (f"Kode\t\t: {temp[1].strip()}")
                print (f"Tahun\t\t: {temp[2].strip()}")
                print (f"Deskripsi\t: {temp[3].strip()}")
    else:
        print (f"Tidak Ditemukan!")