import re

def CountWisnu(Userinp):
    try:
        handle = open(Userinp)
        jb = 0
        jw = 0

        for line in handle:
            hasil = re.findall('Wisnu', line)
            jw += len(hasil)
            jb += 1
            
        print("===============================")
        print("= Kemunculan Wisnu :", jw)
        print("= Jumlah Baris :", jb)
        print("===============================")

    except:
        print("File Tidak Ada Prof")

if __name__ == "__main__":
    userinp = str(input())
    CountWisnu(userinp)