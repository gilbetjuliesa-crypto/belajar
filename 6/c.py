#nama fungsi isi sendiri
def belahketupat(tinggi):
    for i in range(tinggi):
        print(" " * (tinggi - i - 1) + " *" * (i + 1))
    
    for i in range(tinggi - 1,-2,-1):
        print(" " * (tinggi - i - 1) + " *" * (i + 1))
        
if __name__ == "__main__":
    tinggi = int(input())
    belahketupat(tinggi)