fname = input("Enter a file name: ")

fhand = open(fname)

jam_dic = dict()

for baris in fhand:

    if baris.startswith("From "):

        kata = baris.split()

        waktu = kata[5]

        jam = waktu.split(":")[0]

        if jam not in jam_dic:
            jam_dic[jam] = 1
        else:
            jam_dic[jam] += 1

lst = list()

for key, val in jam_dic.items():
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)