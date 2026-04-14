import re
from datetime import datetime

teks = input("Masukkan teks: ")

tanggal_list = re.findall(r'\d{4}-\d{2}-\d{2}', teks)

sekarang = datetime.now()

for tgl in tanggal_list:
    tanggal = datetime.strptime(tgl, "%Y-%m-%d")
    selisih = (sekarang - tanggal).days
    format_baru = tanggal.strftime("%d-%m-%Y")
    print(tanggal, "selisih", selisih, "hari")