def proses(text):
    angka = ""
    
    for c in text:
        if c.isdigit():
            angka += c

    odd = []   
    even = []  

    for d in angka:
        d = int(d)

        if d % 2 == 0:  
            odd.append(str(10 + d))
        else:           
            even.append(str(d + 6))

    print("=========================")

    print(" ODD NUMBER :", end="")
    if odd:
        for x in odd:
            print(x, end=" ")
    print()

    print(" EVEN NUMBER :", end="")
    if even:
        for x in even:
            print(x, end=" ")
    print()

    print("=========================")


if __name__ == "__main__":
    text = input()
    proses(text)