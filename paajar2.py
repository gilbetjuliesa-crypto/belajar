n = int(input("Masukkan n: "))

for i in range(n, 0, -1):
    faktorial = 1
    
    for j in range(i, 0, -1):
        faktorial = faktorial * j
        
    print(faktorial, end=" ")
    
    for k in range(i, 0, -1):
        print(k, end=" ")
        
    print()