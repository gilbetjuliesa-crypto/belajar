import re
from datetime import datetime

def proses_tanggal(teks):
    tanggal_list = re.findall(r'\d{4}-\d{2}-\d{2}', teks)
    sekarang = datetime.now()
    
    for tgl in tanggal_list:
        tanggal = datetime.strptime(tgl, "%Y-%m-%d")
        selisih = (sekarang - tanggal).days
        
        print(tanggal, "selisih", selisih, "hari")

# input
teks = input("Masukkan teks: ")
proses_tanggal(teks)