def klasifikasi(n):
    try:
        n = int(n)
        
        if n < 0:
            print("Negatif")
        elif n == 0:
            print("Nol")
        else:
            if n % 2 == 0:
                print("Genap")
            else:
                print("Ganjil")
    except:
        print("Input tidak valid")

if __name__ == "__main__":
    n = input()
    klasifikasi(n)