#Buat nama fungsi dan parameternya
def cetak(awal, akhir):

    if awal < akhir: 
        for i in range(awal, akhir+1):
            print(i, end=" ")
    else:
        for i in range(awal, akhir-1, -1):
            print(i, end=" ")

if __name__ == "__main__":
    awal = int(input())
    akhir = int(input())
    cetak(awal,akhir)