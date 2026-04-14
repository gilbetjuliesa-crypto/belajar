import re
import random
import string

def buat_password():
    karakter = string.ascii_letters + string.digits
    password = ""
    
    for i in range(8):
        password += random.choice(karakter)
    
    return password

def proses_email(teks):
    emails = re.findall(r'\S+@\S+', teks)
    
    for email in emails:
        username = email.split("@")[0]
        password = buat_password()
        
        print(email, "username:", username, ", password:", password)

# input
teks = input("Masukkan teks: ")
proses_email(teks)