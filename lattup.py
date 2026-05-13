tA = eval(input("Masukkan tuple: "))

sama = True

for item in tA:

    if item != tA[0]:
        sama = False

print(sama)