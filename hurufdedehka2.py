data = list(map(int, input().split()))

data_unik = list(set(data))
data_unik.sort()

print("Terbesar kedua :", data_unik[-2])