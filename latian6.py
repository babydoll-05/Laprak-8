import re
import random
import string

def buat_password():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

def cari_email(teks):
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b', teks)
    for email in emails:
        username = email.split('@')[0]
        print(f"{email} username: {username} , password: {buat_password()}")

teks = """
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

cari_email(teks)