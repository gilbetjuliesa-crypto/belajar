pasake = dict()
pasake = {'satu': 'uno', 'dua': 'dos', 'tiga': 'tres'}
print(pasake) #mengeluarkan pasangan yang ada
print(len(pasake)) #menghitung berapa banyak pasangan 
print(pasake['satu']) #mengeluarkan value dari satu

sampu = list(pasake.values())
'uno' in sampu
print(sampu) #hanya mengeluarkan value

mantap = 'bungul'
f = dict()
for x in mantap:
    if x not in f:
        f[x] = 1
    else:
        f[x] = f[x] + 1
print('keluar: ', f) #mengeluarkan berapa jumlah huruf yang keluar 

coin = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(coin.get('jan', 0)) #mengeluarkan value dari jan
print(coin.get('jin', 0)) #mengeluarkan 0 karena jin tidak ada pada list

#bentuk sederhana:
mantap = 'bungul'
a = dict()
for b in mantap:
    a[b] = a.get(b,0) + 1
print(a)

#teks 
teks = input('masukan nama file: ')
try:
    x = open(teks)
except:
    print('cannot be opened: ', teks)
    exit()

counts = dict()
for line in x:
    word = line.split()
    for well in word:
        if well not in counts:
            counts[well] = 1
        else:
            counts[well] += 1

print(counts)

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key]) #hubungan nilai

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10 :
        print(key, counts[key]) #Hanya menampilkan nilai yang diatas 10


counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key]) # mengeluarkan dalam bentuk list kebawah secara urut berdasarkan a c dan j


