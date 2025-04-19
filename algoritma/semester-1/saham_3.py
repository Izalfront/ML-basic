# harga_saham = [3,3,5,0,0,3,1,4]
# harga_saham = [1,2,3,4,5]
harga_saham = [1,2,4]
total_untung = 0
untung_sebelumnya = 0
count = 0

for i in range(1, len(harga_saham)):
    # disini ada pembatas 2x transaksi
    # cari nilai terendah yang akan dijual ke harga maksimum (di indeks selanjutnya)
    # lalu cari lagi nilai terendah ke-2 lalu jual ke harga maksimum (di indeks selanjutnya)
    # sampai ketemu nilai tertinggi sebelum nilai terendah
    if harga_saham[i] > harga_saham[i-1]:
        untung = harga_saham[i] - harga_saham[i-1]
        total_untung =+ untung

print(total_untung)
# batasi hanya 2x transaksi
# berarti ada code < 3 untuk batas transaksi
# cara membatasi seperti ini [2:]
# [1,2,3,4,5] = 4
# [3,3,5,0,0,3,1,4] = 6
# [7,6,4,3,1] = 0
# (kemungkinan) jika ada harga 0 maka beli dan jual di harga tertinggi besoknya
# [3,3,5,0,0,3,1,4] = beli 0 jual 3 maka 3-1 = 3 dan beli 1 jual 4 maka 4-1 = 3
# day-1 = 3, day-2 = 3, total keuntungan = 3 + 3 = 6
# ---
# harga_saham ini ibaratnya data history, bukan seperti real life saham