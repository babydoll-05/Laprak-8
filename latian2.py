import string
def menghitung_frekuensi(kalimat, kata):
    
    kalimat = kalimat.lower()
    kate = kalimat.split()
    kate = [k.strip(string.punctuation) for k in kate]
    f = kate.count(kata.lower())

    return f

kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata = "makan"
f = menghitung_frekuensi(kalimat, kata)

print(f"{kata} ada {f} buah")