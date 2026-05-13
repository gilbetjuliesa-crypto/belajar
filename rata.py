nilai = eval(input("Masukkan tuple nilai: "))

total = 0

for item in nilai:
    total += item

rata = total / len(nilai)

print(rata)