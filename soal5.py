def soal5(n):
    for i in range(1, n + 1):
        if i % 4 == 0 and i % 6 == 0:
            print("EmpatEnam")
        elif i % 4 == 0:
            print("Empat")
        elif i % 6 == 0:
            print("Enam")
        else:
            print(i)

if __name__ == "__main__":
    n = int(input())
    soal5(n)