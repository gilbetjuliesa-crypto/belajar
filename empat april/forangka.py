def sorting_string(text):
    angka = []

    for c in text:
        if c.isdigit():
            angka.append(int(c))

    angka.sort()

    return " ".join(map(str, angka))


if __name__ == "__main__":
    stript = str(input())
    print(sorting_string(stript))