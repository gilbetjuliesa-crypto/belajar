def skyNet(status_pengguna, jam_buka, jam_masuk, jam_keluar, jam_tutup, waktu_tambahan_member, billing, denda):
    try:
        jam_buka = int(jam_buka)
        jam_masuk = int(jam_masuk)
        jam_keluar = int(jam_keluar)
        jam_tutup = int(jam_tutup)
        waktu_tambahan_member = int(waktu_tambahan_member)
        billing = int(billing)
        denda = int(denda)
    except:
        return "Data nya ada yang ga valid"

    if status_pengguna not in ["M", "U"]:
        return "Status pengguna tidak valid"

    if billing < 0:
        return "Billing harus lebih dari 0!"

    if jam_masuk < jam_buka:
        return "Maaf lab belum buka"

    lama_asli = jam_keluar - jam_masuk

    # 🔥 HANYA FIX DI SINI (>= dan langsung ke lama_asli)
    if jam_keluar >= jam_tutup:
        if status_pengguna == "M":
            lama_asli += waktu_tambahan_member

    if lama_asli < billing:
        sisa = billing - lama_asli
        return f"sisa waktu: {sisa} jam"

    elif lama_asli > billing:
        lebih = lama_asli - billing
        denda_total = lebih * denda
        return f"Anda kena denda sebesar Rp.{denda_total}"

    else:
        return "Terimakasih telah berkunjung ke lab"


if __name__ == '__main__':
    status_pengguna, jam_buka, jam_masuk, jam_keluar, jam_tutup, waktu_tambahan_member, billing, denda = input().split()
    print(skyNet(status_pengguna, jam_buka, jam_masuk, jam_keluar, jam_tutup, waktu_tambahan_member, billing, denda))