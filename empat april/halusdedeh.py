def sorting_string(text):
    hasil = ""
    for i in range(len(text)):
        if text[i].isalpha():
            if i % 2 == 0:
                hasil += text[i].lower()
            else:
                hasil += text[i].upper()
        else:
            hasil += text[i]

    return hasil


if __name__ == "__main__":
    stript = str(input())
    print(sorting_string(stript))