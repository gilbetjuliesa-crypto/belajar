def cek_prima(n, i):
    if n <= 1:
        return False
    
    if i == 1:
        return True
    
    if n % i == 0:
        return False

    # Recursive case
    return cek_prima(n, i - 1)

angka = int(input("Masukkan bilangan: "))

if cek_prima(angka, angka - 1):
    print(angka, "adalah bilangan PRIMA")
else:
    print(angka, "bukan bilangan PRIMA")