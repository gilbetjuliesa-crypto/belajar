def prima(n):
    if n <= 1:
        print("Bukan prima")
        return
    
    for i in range(2, n):
        if n % i == 0:
            print("Bukan prima")
            return
    
    print("Prima")

if __name__ == "__main__":
    n = int(input())
    prima(n)