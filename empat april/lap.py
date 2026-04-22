import re

teks = "Nomor saya adalah 08123456789"

cari = re.search(r'\d+', teks)

if cari:
    print(cari.group())

    