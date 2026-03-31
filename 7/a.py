#nama fungsi dan parameter serta isi fungsinya
def pakarai(n):
    try:
        n = int(n) 
        if n < 0:
            print("Negatif Cokk")
        elif n == 0:
            print("Endog")
        
        for i in range(1, n + 1):
            if n > 0:
                if i % 3 == 0 and i % 5 ==0:
                    print("Ayoyoyo")
                elif i % 2 == 0:
                    print("Genap Cokk")
                else:
                    print("Ganjil Cokk")
    except:
        print("Apehal ni Prof")
if __name__ == "__main__":
    userint = input()
    pakarai(userint)