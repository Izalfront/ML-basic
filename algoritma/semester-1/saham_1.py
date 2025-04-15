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

beli = 0
jual = len(harga_saham) - 1
target = 2

while beli < jual:
    profit = harga_saham[jual] - harga_saham[beli]
    print(f"Profit {harga_saham[jual]} - {harga_saham[beli]} = {profit}")

    if profit == target:
        print(f"Ketemu! {harga_saham[jual]} - {harga_saham[beli]} = {target}")
        break
    elif profit < target:
        beli += 1
    elif profit > target:
        jual -= 1
else:
    print("Tidak ada pasangan yang ditemukan")


