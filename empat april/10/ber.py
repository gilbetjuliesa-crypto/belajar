a = int(input('Masukkan tinggi berlian\t: '))
b = open("Berlian.txt","x")
with open('Berlian.txt', 'w') as teks1:
    for i in range(1, (a//2)+1):
        teks1.write(" "*(a-i-2))
        teks1.write("*"*i)
        teks1.write("*"*(i-1))
        teks1.write('\n')
    for j in range((a//2)+1, 0, -1):
        teks1.write(" "*(a-j-2))
        teks1.write("*"*j)
        teks1.write("*"*(j-1))
        teks1.write('\n')