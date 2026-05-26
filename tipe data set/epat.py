def jumlah_digit(n):
    if n < 10:
        return n
    else:
        return (n % 10) + jumlah_digit(n // 10)

angka = 234
print("Jumlah digit:", jumlah_digit(angka))