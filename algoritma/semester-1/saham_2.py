# harga_saham = [7,1,5,3,6,4]
harga_saham = [1,2,3,4,5]
# masalahnya ada di index 0 jika lebih besar dari index 1 maka jawaban benar hasilnya 4. 
# (tapi dia menjual value 3. dua kali ke index selanjutnya)
# tapi masalahnya array nya seperti ini [1,2,3,4,5] jadinya dia cetak value 1 terus untuk harga termurah
# butuh validasi dulu agar dia mulai dari index selanjutnya, bukan dari index awal lagi

beli = harga_saham[0]
untung_terbesar = 0
list_untung = []
total_untung = 0

beli_2 = harga_saham[0]
untung_terbesar_2 = 0

for harga in harga_saham:
    if untung_terbesar == 0:
        if harga < beli:
            beli = harga
            print(f"Beli di harga terkecil {beli}")
        if harga - beli > untung_terbesar:
            untung_terbesar = harga - beli
            print(f"Jual di harga tertinggi {harga}")
            print(f"Untung {harga - beli}")
            list_untung.append(harga - beli)
    else:
        if harga < beli_2:
            beli_2 = harga
            print(f"2. harga termurah adalah: ", beli_2)
        if harga - beli_2 > untung_terbesar_2:
            untung_terbesar_2 = harga - beli_2
            print(f"2. Jual di harga tertinggi {harga}")
            print(f"2. Untung {harga - beli_2}")
            list_untung.append(harga - beli_2)

for i in list_untung:
    total_untung += i
print(f"Total keuntungan adalah {total_untung}")

# 1x beli dan 1x jual dan ambil keuntungan. lalu di array selanjutnya beli lagi dan jual lagi 1x
# setelah itu jumlahkan semua keuntungan dari setiap transaksi