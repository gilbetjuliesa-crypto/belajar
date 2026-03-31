def terkecil(list_angka):
    return min(list_angka)

# Jangan dirubah
if __name__ == "__main__":
    angka = input().split()
    listangka = []
    for i in angka:
        if i.isdigit():
            listangka.append(int(i))
        else:
            continue
    print(terkecil(listangka))