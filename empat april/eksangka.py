def sorting_string(text):
    kata = text.split()
    valid = []

    for k in kata:
        if k.isdigit() and len(k) == 4 and k[0] != "0":
            valid.append(k)

    return "Valid: " + ", ".join(valid) if valid else "Tidak ada"


if __name__ == "__main__":
    stript = str(input())
    print(sorting_string(stript))