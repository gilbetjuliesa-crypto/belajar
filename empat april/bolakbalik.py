def sorting_string(text):
    huruf = [c for c in text if c.isalpha()]
    huruf.reverse()

    hasil = ""
    idx = 0

    for c in text:
        if c.isalpha():
            hasil += huruf[idx]
            idx += 1
        else:
            hasil += c

    return hasil


if __name__ == "__main__":
    stript = str(input())
    print(sorting_string(stript))