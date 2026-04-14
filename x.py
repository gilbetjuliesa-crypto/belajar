def polaX(n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    n = int(input())
    polaX(n)