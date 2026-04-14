def hurufG(lebar, tinggi):
    if tinggi % 2 == 0 or tinggi < 3 or lebar < 3:
        print("Tidak valid")
        return
    
    tengah = tinggi // 2
    
    for i in range(tinggi):
        for j in range(lebar):
            if i == 0 or i == tengah or i == tinggi - 1:
                print("#", end=" ")
            elif j == 0:
                print("#", end=" ")
            elif i >= tengah and j == lebar - 1:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    lebar = int(input())
    tinggi = int(input())
    hurufG(lebar, tinggi)