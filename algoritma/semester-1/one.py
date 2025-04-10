angka = [-2,1,-3,4,-1,2,1,-5,4]
angka_unik = []
# menghapus nilai duplikat dan mengurutkan dari terbesar
for index in angka:
    if index not in angka_unik:
        angka_unik.append(index)
            
hasil1 = sorted(angka_unik, reverse=False)
print(hasil1)

# menyeleksi hanya angka terbesar saja
seleksi_angka = []

for index in hasil1:
    if index > -2:
        seleksi_angka.append(index)

print(seleksi_angka)

# menjumlahkan isi array
jumlah = sum(seleksi_angka)
print(jumlah)
