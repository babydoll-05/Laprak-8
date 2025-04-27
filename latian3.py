def menghapus_spasi(x):
    kate = x.split()
    teks_baru = ' '.join(kate)
    return teks_baru

x = "saya tidak suka memancing ikan "

print(menghapus_spasi(x))