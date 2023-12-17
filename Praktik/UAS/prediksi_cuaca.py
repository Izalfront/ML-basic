from sklearn.neighbors import KNeighborsClassifier

 #Data training ( dari WEBSITE BMKG CUACA)
data_training = [
    [28, 70, 15, 'Cerah'],
    [25, 80, 12, 'Cerah'],
    [20, 90, 8, 'Hujan'],
    [18, 85, 10, 'Hujan'],
    [30, 60, 5, 'Cerah'],
    [22, 75, 9, 'Hujan'],
    [26, 65, 14, 'Cerah'],
    [22, 80, 6, 'Berawan'],
    [32, 55, 3, 'Cerah'],
    [19, 75, 11, 'Hujan'],
    [23, 70, 7, 'Berawan'],
    [27, 65, 13, 'Berawan'],
    [29, 60, 4, 'Cerah'],
    [17, 85, 16, 'Hujan'],
    [21, 75, 10, 'Hujan']
]

# Memisahkan atribut dan label dari data training
atribut = [[data[0], data[1], data[2]] for data in data_training]
label = [data[3] for data in data_training]

# Membuat model k-NN dengan K-3
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(atribut, label)

# Inputan data cuaca baru yang ingin diprediksi
suhu = int(input("Masukkan suhu (derajat Celsius): "))
kelembapan = int(input("Masukkan kelembapan (persen): "))
kecepatan_angin = int(input("Masukkan kecepatan angin (km/jam): "))
jam = int(input("Masukkan jam (0-23): "))

# Melakukan prediksi cuaca berdasarkan data cuaca baru
data_cuaca_baru = [[suhu, kelembapan, kecepatan_angin]]
hasil_prediksi = knn_model.predict(data_cuaca_baru)

# Menampilkan hasil prediksi
print("Hasil prediksi cuaca:", hasil_prediksi[0])
