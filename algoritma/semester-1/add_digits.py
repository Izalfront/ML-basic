inputs = 387

while inputs > 9:
    angka1 = inputs % 10
    angka2 = inputs // 10
    inputs = angka1 + angka2

print('hasilnya: ',inputs)