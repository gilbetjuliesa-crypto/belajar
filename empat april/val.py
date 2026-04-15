def sorting_string(text):
    ada_besar = False
    ada_kecil = False
    ada_angka = False

    for c in text:
        if c.isupper():
            ada_besar = True
        elif c.islower():
            ada_kecil = True
        elif c.isdigit():
            ada_angka = True

    if ada_besar and ada_kecil and ada_angka and len(text) >= 8:
        return "Valid Password"
    else:
        return "Tidak Valid"


if __name__ == "__main__":
    stript = str(input())
    print(sorting_string(stript))