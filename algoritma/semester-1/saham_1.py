# 1. day tergantung index di array. index-0 = day 1
# 2. di array [7,1,5,3,6,4] ini adalah harga saham
# index-0 = day 1, harga saham 7.
# 3. jika beli di index-0 dan jual di index-1 maka
# 1-7=-6 ( sell - buy = result )
# -----
# step 1: beli di day-2 harga: 1
# step 2: jual di day-5 harga: 6
# step 3: profit = 6-1=5
harga_saham = [7,1,5,3,6,4]

beli = harga_saham[0]
untung_terbesar = 0

for harga in harga_saham:
    if harga < beli:
        beli = harga
        print(f"Beli di harga terkecil {beli}")
    elif harga - beli > untung_terbesar:
        untung_terbesar = harga - beli
        print(f"Jual di harga tertinggi {harga}")
        print(f"Untung {harga - beli}")
print(f"Untung terbesar adalah {untung_terbesar}")



