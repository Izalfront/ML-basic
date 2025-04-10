
nums = [1,1,2,2,3]
angka_unik = []

for index in nums:
    if index not in angka_unik:
        angka_unik.append(index)
                
print(sorted(angka_unik, reverse=False))