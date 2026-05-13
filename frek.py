angka = eval(input("Masukkan tuple angka: "))

dic = dict()

for item in angka:

    if item not in dic:
        dic[item] = 1
    else:
        dic[item] += 1

for key, val in dic.items():
    print(key, val)