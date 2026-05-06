def prof(data):
    x = set(data.keys())
    y = set()

    for z in data.values():
        y.update(z)

    hasil = list(x - y)
    hasil.sort()
    return hasil

data = eval(input("Masukkan data: "))


hasil = prof(data)

print(hasil)

