def analisis_nilai(data):

    tertinggi = data[0]

    total = 0

    for nama, nilai in data:

        total += nilai

        if nilai > tertinggi[1]:
            tertinggi = (nama, nilai)

    rata = total / len(data)

    urut = list(data)

    urut.sort(key=lambda x: x[1], reverse=True)

    print("Siswa Terbaik :", tertinggi[0])
    print("Rata-rata :", rata)
    print("Urutan Nilai :")
    print(tuple(urut))

data_siswa = eval(input("Masukkan data siswa : "))

analisis_nilai(data_siswa)