satu = "Step! on, no.. pets??"
satu = satu.lower()

satu = ''.join([i for i in satu if i.isalpha()]) #buang semua yang bukan alfabet
print(satu)
dua = satu[::-1]
print(dua)
if dua == satu:
    print("palindrom")
else:
    print("bukan")
