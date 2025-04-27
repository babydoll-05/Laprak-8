def cari_terpanjang_terpendek(kalimat):
    kate = kalimat.split()
    kata_terpendek = kata_terpanjang = kate[0]
    for kata in kate:
        if len(kata) < len(kata_terpendek):
            kata_terpendek = kata
        elif len(kata) > len(kata_terpanjang):
            kata_terpanjang = kata
    return kata_terpendek, kata_terpanjang

kalimat = "red snakes and a black frog in the pool"
kata_terpendek, kata_terpanjang = cari_terpanjang_terpendek(kalimat)
print(f"terpendek: {kata_terpendek}, terpanjang: {kata_terpanjang}")