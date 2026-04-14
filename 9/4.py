kalimat = input("Masukkan kalimat: ")

kalimat = kalimat.replace(".", "")

kata_kata = kalimat.split()

terpendek = kata_kata[0]
terpanjang = kata_kata[0]

for kata in kata_kata:
    if len(kata) < len(terpendek):
        terpendek = kata
    if len(kata) > len(terpanjang):
        terpanjang = kata

print("Kata terpendek:", terpendek)
print("Kata terpanjang:", terpanjang)