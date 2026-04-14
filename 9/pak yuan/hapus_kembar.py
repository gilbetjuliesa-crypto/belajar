def hapus_kembar(kata):
	jawaban= ""
	for i in range(len(kata)-1):
		if kata[i] != kata[i+1]:
			jawaban = jawaban + kata[i]
	jawaban = jawaban + kata[-1]
	return jawaban
	
kata = input("masukan sebuah string: ")
hasil = hapus_kembar(kata)
print(f"setelah dihapus: {hasil}")