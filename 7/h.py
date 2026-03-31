def hitung_nilai():
    n = int(input("Jumlah mahasiswa: "))
    
    for i in range(n):  
        print(f"Mahasiswa ke-{i+1}")
        
        nilai = int(input("Masukkan nilai: "))
        
        if nilai >= 85:
            grade = "A"
        elif nilai >= 70:
            grade = "B"
        elif nilai >= 60:
            grade = "C"
        elif nilai >= 50:
            grade = "D"
        else:
            grade = "E"
        
        if grade == "A" or grade == "B":
            status = "Lulus"
        else:
            status = "Tidak Lulus"
        
        print("Grade:", grade)
        print("Status:", status)
        print("-" * 20)


hitung_nilai()