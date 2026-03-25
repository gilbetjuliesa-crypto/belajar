def hurufF(mendatar, menurun):
    if menurun % 2 == 0 or mendatar < 3:
        print("Maaf Prof")
    else:
        tengah = menurun // 2 + 1

        for i in range(1, menurun + 1):
            for j in range(1, mendatar + 1):
                if i == 1 or i == tengah:
                    print("#", end=" ")
                else:
                    if j == 1:
                        print("#", end=" ")
                    else:
                        print(" ", end=" ")
            print()


if __name__ == "__main__":
    mendatar = int(input())
    menurun = int(input())
    hurufF(mendatar, menurun)