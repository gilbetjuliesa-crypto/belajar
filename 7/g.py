def angkaG(mendatar, menurun):
    # cek syarat
    if menurun % 2 == 0 or menurun < 3 or mendatar < 3:
        print("Izinnn")
        return

    tengah = menurun // 2  # bagian tengah

    for i in range(menurun):
        for j in range(mendatar):
            # baris atas
            if i == 0:
                print("#", end=" ")
            # baris tengah
            elif i == tengah:
                print("#", end=" ")
            # baris bawah
            elif i == menurun - 1:
                print("#", end=" ")
            # kiri
            elif j == 0:
                print("#", end=" ")
            # kanan (bagian G)
            elif i >= tengah and j == mendatar - 1:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    mendatar = int(input())
    menurun = int(input())
    angkaG(mendatar, menurun)