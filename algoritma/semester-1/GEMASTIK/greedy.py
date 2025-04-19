n = int(input())
angka = list(map(int, input().split()))

total_seharusnya = n * (n + 1) // 2
total_diberikan = sum(angka)

hilang = total_seharusnya - total_diberikan
print(hilang)
