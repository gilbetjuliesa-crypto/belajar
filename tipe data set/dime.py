def kombinasi(n, r):
    if r == 0 or r == n:
        return 1
    else:
        return kombinasi(n-1, r-1) + kombinasi(n-1, r)

n = int(input("Masukkan nilai n: "))
r = int(input("Masukkan nilai r: "))

print("Hasil kombinasi C(", n, ",", r, ") =", kombinasi(n, r))