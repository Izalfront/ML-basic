arr1 = [1,2,3]
arr2 = [4,5,6]

for i in arr1:
    arr2.append(i)

hasil = sorted(arr2)  # Output: [4, 5, 6, 1, 2, 3] di sorted [1,2,3,4,5,6]
jumlah = len(hasil)  # Output: 28

if jumlah % 2 == 0:
    median_1 = jumlah // 2 - 1
    median_2 = median_1 + 1
    median = (hasil[median_1] + hasil[median_2]) / 2.0
else:
    median = hasil[jumlah // 2]

print("Hasil:", median)