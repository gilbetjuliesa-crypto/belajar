def f(x):
    return (x**2) + (2*x) + 3

x = int(input())

hasil = f(f(f(x)+x)+f(f(x)))
print(hasil)