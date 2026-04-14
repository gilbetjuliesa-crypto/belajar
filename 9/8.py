def cek_anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()
    
    if len(kata1) != len(kata2):
        return "Bukan Anagram"
    
    for huruf in kata1:
        if kata1.count(huruf) != kata2.count(huruf):
            return "Bukan Anagram"
    
    return "Anagram"

k1 = input("Kata 1: ")
k2 = input("Kata 2: ")

print(cek_anagram(k1, k2))