# harga_saham = [7,1,5,3,6,4]

# masalahnya ada di index 0 jika lebih besar dari index 1 maka jawaban benar hasilnya 4. 
# (tapi dia menjual value 3. dua kali ke index selanjutnya)
# tapi masalahnya array nya seperti ini [1,2,3,4,5] jadinya dia cetak value 1 terus untuk harga termurah
# butuh validasi dulu agar dia mulai dari index selanjutnya, bukan dari index awal lagi
# ---
# harus 1x looping untuk dapat nilai akhir total semua keuntungan misal [1,2,3,4,5] = 4
# beli = harga_saham[0]
# untung_terbesar = 0
# harga_saham = [1,2,3,4,5]
harga_saham = [1,2,4]
total_untung = 0

for i in range(1, len(harga_saham)):
    if harga_saham[i] > harga_saham[i-1]:
        untung = harga_saham[i] - harga_saham[i-1]
        total_untung += untung
print(total_untung)        
        

# 1x beli dan 1x jual dan ambil keuntungan. lalu di array selanjutnya beli lagi dan jual lagi 1x
# setelah itu jumlahkan semua keuntungan dari setiap transaksi