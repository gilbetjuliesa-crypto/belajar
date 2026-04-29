data = list(map(int, input().split()))

genap = []
ganjil = []

for i in data:
    if i % 2 == 0:
        genap.append(i)
    else:
        ganjil.append(i)

print("Genap :", genap)
print("Ganjil :", ganjil)