def banyak_kaleng_cat(panjang, lebar, jari):
    x = ( panjang * lebar ) + ((1/2)*3.14*jari**2)
    y = x/15
    return round(y)