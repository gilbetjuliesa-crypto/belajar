def deret_gws(jumlah_bilangan, kelipatan, angka_gws1, angka_gws2, kata_gws1, kata_gws2, kata_gws_spesial):
    try:
        jumlah_bilangan = int(jumlah_bilangan)
        kelipatan = int(kelipatan)
        angka_gws1 = int(angka_gws1)
        angka_gws2 = int(angka_gws2)
        bilangan = 0
        if jumlah_bilangan > 0 and kelipatan > 0 and angka_gws1 > 0 and angka_gws2 > 0 and angka_gws1 <= jumlah_bilangan and angka_gws2 <= jumlah_bilangan:
           for i in range(jumlah_bilangan):
                bilangan = bilangan + kelipatan 
                if bilangan % angka_gws1 == 0 and bilangan % angka_gws2 == 0:
                    print(kata_gws_spesial, end=" ")
                elif bilangan % angka_gws1 == 0:
                    print(kata_gws1, end=" ")
                elif bilangan % angka_gws2 == 0:
                    print(kata_gws2, end=" ")
                else:
                    print(bilangan, end=" ")      
        else:
            print("TIDAK VALID") 
    except:
        print("TIDAK VALID")
       
    
bil, kel, gws1, gws2, k1, k2, k_spesial = input().split()
deret_gws(bil, kel, gws1, gws2, k1, k2, k_spesial)
