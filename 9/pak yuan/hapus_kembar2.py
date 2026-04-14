def hapus_kembar(kata):
    if kata == "":
        return ""
        
    jawaban= ""
    for i in range(len(kata)-1):
        if kata[i] != kata[i+1]:
            jawaban = jawaban + kata[i]
    jawaban = jawaban + kata[-1]
    return jawaban


def hapus_kembar_rekursif(kata, jawaban=""):
    if kata == "":
        return jawaban
        
    if len(kata) == 1:
        jawaban = jawaban + kata
        return jawaban
    elif len(kata) == 2:
        if kata[0] == kata[1]:
            jawaban = jawaban + kata[0]
        else:
            jawaban = jawaban + kata
        return jawaban
    else:
        if kata[0] == kata[1]:
            return hapus_kembar_rekursif(kata[1:], jawaban)
        else:
            return hapus_kembar_rekursif(kata[1:], jawaban + kata[0])


kata = input("masukan sebuah string: ")

hasil = hapus_kembar(kata)
hasil2 = hapus_kembar_rekursif(kata)

print(f"iteratif: {hasil}")
print(f"rekursif: {hasil2}")