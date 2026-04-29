data = list(map(int, input().split()))

unik = []

for i in data:
    if i not in unik:
        unik.append(i)

print("Data tanpa duplikat :", unik)