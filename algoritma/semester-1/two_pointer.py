data = [1,2,3,5]

kiri = 0
kanan = len(data) - 1

target = 3

while kiri < kanan:
    jumlah = data[kiri] + data[kanan]
    print(f"Jumlah {data[kiri]} + {data[kanan]} = {jumlah}")

    if jumlah == target:
        print(f"Ketemu! {data[kiri]} + {data[kanan]} = {target}")
        break
    elif jumlah < target:
        kiri += 1
    elif jumlah > target:
        kanan -= 1
else:
    print("Tidak ada pasangan yang ditemukan")
