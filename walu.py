def angka8(mendatar, menurun):
    if menurun % 2 == 0 or menurun < 5 or mendatar < 3:
        print("Izininn")
    else:
        tengah = menurun // 2 + 1

        for i in range(1, menurun + 1):
            for j in range(1, mendatar + 1):
                if i == 1 or i == tengah or i == menurun:
                    print("#", end="")
                else:
                    if j == 1 or j == mendatar:
                        print("#", end="")
                    else:
                        print(" ", end="")

                if j != mendatar:
                    print(" ", end="")
            print()


if __name__ == "__main__":
    mendatar = int(input())
    menurun = int(input())
    angka8(mendatar, menurun)