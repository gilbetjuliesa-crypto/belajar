a = int(input())
b = input()
c = input()
hasil = 0

for i in range(a):
    if b[i] == 'M'  and c[i] == 'M':
        hasil += 1
print(hasil)