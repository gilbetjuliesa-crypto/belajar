import re
import random
import string

teks = input("Masukkan teks: ")

emails = re.findall(r'\S+@\S+', teks)

for email in emails:
    username = email.split("@")[0]
    
    karakter = string.ascii_letters + string.digits
    password = ""
    for i in range(8):
        password += random.choice(karakter)
    
    print(email, "username:", username, ", password:", password)