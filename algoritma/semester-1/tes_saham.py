# harga_saham = [1,2,4]
harga_saham = [1,2,3,4,5]
total_untung = 0


for i in range(1, len(harga_saham)):
    # pembatas jual-beli 2x saja
    if harga_saham[i] > harga_saham[i-1]:
        untung = harga_saham[i] - harga_saham[i-1]
        total_untung += untung
        print(total_untung)


