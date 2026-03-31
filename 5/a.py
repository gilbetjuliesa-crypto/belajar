def konversi_waktu(jam, menit, format_24):
    if jam < 0 or jam > 24 or menit < 0 or menit > 59:
        return "Opo iki"
    
    if jam == 24 and menit != 0:
        return "Opo iki"
        
    if format_24:
        if jam == 24:
            jam = 0
        return f"Jam : {jam:02d}:{menit:02d}"
    else:
        if jam == 0 or jam == 24:
            jam_12 = 12
            periode = "AM"
        elif jam < 12:
            jam_12 = jam
            periode = "AM"
            return f"Jam : {jam_12:02d}:{menit:02d} {periode}"
        elif jam == 12:
            jam_12 = 12 
            periode = "PM"
        else:
            jam_12 = jam - 12 
            periode = "PM"
    
        return f"Jam : {jam_12}:{menit:02d} {periode}"

# BAGIAN INI TIDAK USAH DI UBAH
if __name__ == "__main__":
    jam = int(input())
    menit = int(input())
    format = input()
    fformat = True if format == "true" else False
    print(konversi_waktu(jam,menit,fformat))