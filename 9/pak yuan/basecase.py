def tulisan(n):
    for i in range(n, 0, -1):
        print(i)

def tulisan_rekursif(n):
    if n == 0:
        return
    else:
        print(n)
        tulisan_rekursif(n-1)

tulisan_rekursif(6)