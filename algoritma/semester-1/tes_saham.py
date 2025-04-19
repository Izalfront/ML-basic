harga_saham = [3,3,5,0,0,3,1,4]
# harga_saham = [1,2,4]
# harga_saham = [1,2,3,4,5]
total_untung = 0
harga_sekarang = harga_saham[0]
keuntungan_tertinggi = harga_saham[0]
harga_termurah = harga_saham[0]

for i in range(1, len(harga_saham)):
    if harga_sekarang + harga_saham[i] > harga_saham[i]:
        harga_sekarang = harga_saham[i]
        print(f"harga sekarang: {harga_sekarang}")
    else:
        harga_sekarang = harga_saham[i]
        print(f"harga sekarang kena else: {harga_sekarang}")

    if harga_saham[i] < harga_termurah:
        harga_termurah = harga_saham[i]

    if harga_sekarang > keuntungan_tertinggi:
        keuntungan_tertinggi = harga_sekarang
        print(f"keuntungan tertinggi: {keuntungan_tertinggi}")
    
total_untung = keuntungan_tertinggi - harga_termurah
print(f"total_untung: {total_untung}")
print(f"harga termurah: {harga_termurah}")



