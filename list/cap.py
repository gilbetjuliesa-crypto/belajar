domain_count = {}

fname = input("Masukkan nama file: ")

try:
    fhand = open(fname)
except:
    print("File tidak bisa dibuka")
    exit()

for line in fhand:
    words = line.split()
    
    if len(words) < 2 or words[0] != "From":
        continue
    
    email = words[1]
    
    bagian = email.split("@")
    domain = bagian[1]
    
    if domain not in domain_count:
        domain_count[domain] = 1
    else:
        domain_count[domain] += 1

print(domain_count)