def huruft(mendatar, menurun):
    if mendatar % 2 == 1:
        print("# "* mendatar)
        for i in range (1, menurun):
            print(" "*(mendatar-1), end ='') 
            print("# ")
    else:
        print("Maaf Prof")


if __name__ == "__main__":
    mendatar = int(input())
    menurun = int(input())
    huruft(mendatar,menurun)