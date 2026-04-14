def soal2(n, a, b):
    hasil = 0
    
    for i in range(n):
        if a[i] == b[i]:
            hasil += 1
    
    print(hasil)

if __name__ == "__main__":
    n = int(input())
    a = input()
    b = input()
    
    soal2(n, a, b)