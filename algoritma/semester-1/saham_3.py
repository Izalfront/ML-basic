harga_saham = [3,3,5,0,0,3,1,4]
total_untung = 0

for i in range(1, len(harga_saham)):
    if harga_saham[i] > harga_saham[i-1]:
        untung = harga_saham[i] - harga_saham[i-1]
        total_untung += untung
        print(total_untung)    

# batasi hanya 2x transaksi
# berarti ada code < 3 untuk batas transaksi