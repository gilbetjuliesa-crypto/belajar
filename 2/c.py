usd = int(input())
rupiah = 20000 * usd
gaji = 10000000
total_pengeluaran = 5000000

#menghitung_potongan 
total_potongan_gaji = 10000000 - 1000000

#menghitung pengeluaran 
total = total_potongan_gaji - total_pengeluaran + rupiah
total_keseluruhan = total - (total * 17 / 100)
print (total_keseluruhan)
