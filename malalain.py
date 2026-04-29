kalimat = input().lower().split()

unik = []

for kata in kalimat:
    if kalimat.count(kata) == 1:
        unik.append(kata)

print("Kata unik :", " ".join(unik))