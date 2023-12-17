from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# Data training (dari WEBSITE BMKG CUACA)
data_training = [
    [28, 70, 15, 'Cerah', 'Siang'],  # [suhu, kelembapan, kecepatan_angin, output cuaca, waktu]
    [25, 80, 12, 'Cerah', 'Siang'],
    [20, 90, 8, 'Hujan', 'Malam'],
    [18, 85, 10, 'Hujan', 'Malam'],
    [30, 60, 5, 'Cerah', 'Siang'],
    [22, 75, 9, 'Hujan', 'Siang'],
    [26, 65, 14, 'Cerah', 'Siang'],
    [22, 80, 6, 'Berawan', 'Siang'],
    [32, 55, 3, 'Cerah', 'Malam'],
    [19, 75, 11, 'Hujan', 'Siang'],
    [23, 70, 7, 'Berawan', 'Siang'],
    [27, 65, 13, 'Berawan', 'Siang'],
    [29, 60, 4, 'Cerah', 'Malam'],
    [17, 85, 16, 'Hujan', 'Malam'],
    [21, 75, 10, 'Hujan', 'Malam'],
    [23, 80, 2, 'Berawan', 'Pagi'],
    
]

# Memisahkan atribut dan label dari data training
atribut = [[data[0], data[1], data[2], data[4]] for data in data_training]
label = [data[3] for data in data_training]
waktu = [data[4] for data in data_training]

# Membuat model k-NN dengan K=3
knn_model = KNeighborsClassifier(n_neighbors=3)

# Label encoding untuk mengonversi label string menjadi nilai numerik
label_encoder = LabelEncoder()
label_encoder.fit(label)
label_encoded = label_encoder.transform(label)

waktu_encoder = LabelEncoder()
waktu_encoder.fit(waktu)
waktu_encoded = waktu_encoder.transform(waktu)

# Menggabungkan atribut dan waktu yang telah diubah ke dalam satu array
atribut_waktu = [[atribut[i][0], atribut[i][1], atribut[i][2], waktu_encoded[i]] for i in range(len(atribut))]

knn_model.fit(atribut_waktu, label_encoded)

# Inputan data cuaca baru yang ingin diprediksi
suhu = int(input("Masukkan suhu (derajat Celsius): "))
kelembapan = int(input("Masukkan kelembapan (persen): "))
kecepatan_angin = int(input("Masukkan kecepatan angin (km/jam): "))
jam = int(input("Masukkan jam (0-23): "))

# Menentukan waktu berdasarkan jam
if jam >= 0 and jam < 6:
    waktu = 'Pagi'
elif jam >= 6 and jam < 18:
    waktu = 'Siang'
elif jam >= 18 and jam < 23:
    waktu = 'Malam'
else:
    waktu = 'inputan anda salah'

# Melakukan label encoding pada waktu
waktu_encoded = waktu_encoder.transform([waktu])

# Melakukan prediksi cuaca berdasarkan data cuaca baru
data_cuaca_baru = [[suhu, kelembapan, kecepatan_angin, waktu_encoded[0]]]
hasil_prediksi_encoded = knn_model.predict(data_cuaca_baru)

# Mengembalikan nilai prediksi menjadi label awal (string)
hasil_prediksi = label_encoder.inverse_transform(hasil_prediksi_encoded)

# Menampilkan hasil prediksi
print("Hasil prediksi cuaca pada", waktu, "hari ini:", hasil_prediksi[0])
