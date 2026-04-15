def sorting_string(text):
    huruf = ""
    angka = ""

    for c in text:
        if c.isalpha():
            huruf += c
        elif c.isdigit():
            angka += c

    return "Huruf: " + huruf + "\nAngka: " + angka


if __name__ == "__main__":
    stript = str(input())
    print(sorting_string(stript))