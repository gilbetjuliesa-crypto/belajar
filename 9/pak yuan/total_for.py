def total_for(n):
	jumlah = 0;
	for i in range(1, n+1):
		jumlah = jumlah + i
	return jumlah
	
def total_rumus(n):
	jumlah = int((n +1) * (n/2))
	return jumlah
	
def total_rekursif(n):
	if n == 1:
		return 1
	else:
		return total_rekursif(n-1) + n
		
print(total_for(100))
print(total_rumus(100))
print(total_rekursif(100))