import re
from datetime import datetime

def hitung_selisih_tanggal(teks):
    tanggal_regex = r'\d{4}-\d{2}-\d{2}'
    tanggal_list = re.findall(tanggal_regex, teks)
    sekarang = datetime.now()

    for tgl in tanggal_list:
        tgl_obj = datetime.strptime(tgl, '%Y-%m-%d')
        selisih = (sekarang - tgl_obj).days
        tgl_ubah = tgl_obj.strftime('%Y-%m-%d 00:00:00')
        print(f"{tgl_ubah} selisih {selisih} hari")

teks = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""

hitung_selisih_tanggal(teks)