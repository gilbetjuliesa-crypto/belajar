from collections import defaultdict
def yel(x):
    return x * (x + 1) // 2

def oke():
    x = int(input())
    y = defaultdict(int)
    z = list(map(int, input().split))

    for a in z:
        y[a] += 1

    b = 0

    for value in y.values():
        b += yel(value - 1)

    print(b)

def yel2():
    x = int(input())
    g = list(map(int, input().split()))

    b = 0
    
    for i in range(x):
        for j in range(i + 1, x):
            if g[j] == g[i]:
                b += 1

    print(b)

yel2()


