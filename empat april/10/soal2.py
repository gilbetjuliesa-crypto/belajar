def menang(a, b):
    if a == 'H' and b == 'S':
        return True
    if a == 'S' and b == 'P':
        return True
    if a == 'P' and b == 'H':
        return True
    return False


def solve(nama_file):
    try:
        with open(nama_file) as f:
            N = int(f.readline())
            data = [tuple(map(int, line.split())) for line in f]

        from itertools import permutations

        simbol = ['H', 'P', 'S']
        angka = [1, 2, 3]

        max_menang = 0

        for perm in permutations(simbol):
            mapping = {angka[i]: perm[i] for i in range(3)}

            menang_count = 0

            for a, b in data:
                if menang(mapping[a], mapping[b]):
                    menang_count += 1

            max_menang = max(max_menang, menang_count)

        print(max_menang)

    except:
        print("File Tidak Ada Prof")

nama = input("")
solve(nama)