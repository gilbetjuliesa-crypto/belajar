def soal1(n):
    try:
        n = int(n)
        if n < 0:
            print("Input tidak valid")
            return
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("ABC")
            elif i % 2 == 0:
                print("Genap")
            else:
                print("Ganjil")
    except:
        print("Error input")

if __name__ == "__main__":
    n = input()
    soal1(n)