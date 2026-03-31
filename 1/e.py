import math

def hitung(n: int) -> int:
    hasil = 1 
    for i in range (1, n + 1):
        hasil*= i
    return hasil
    