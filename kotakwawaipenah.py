def persegipanjang(panjang, lebar):
    if panjang % 2 == 0 and lebar % 2 == 0:
        print("Sorry Prof")
    else:
        for i in range(1, lebar+ 1):
            if i % 2 == 1:
                print("# " * panjang)
            else:
                for j in range(1, panjang+1):
                    if j % 2 == 1:
                        print("# ", end="")
                    else: 
                        print(" ", end=" ")
                print("")

if __name__ == "__main__":
    panjang = int(input())
    lebar = int(input())
    persegipanjang(panjang, lebar)