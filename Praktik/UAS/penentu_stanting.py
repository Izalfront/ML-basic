def hitung_bmi(berat_badan, tinggi_badan):
    # Menghitung BMI
    tinggi_badan_m = tinggi_badan / 100  # Konversi tinggi badan dari cm ke meter
    bmi = berat_badan / (tinggi_badan_m ** 2)
    return bmi

def tentukan_kategori_stanting(umur_bulan, bmi):
    # Tentukan kategori stanting berdasarkan umur dan BMI
    if umur_bulan <= 60:  # Umur 0-60 bulan (0-5 tahun)
        if bmi < 16:
            return "Kurus Parah"
        elif 16 <= bmi < 17:
            return "Kurus Sedang"
        elif 17 <= bmi < 18.5:
            return "Kurus Ringan"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Kelebihan Berat Badan"
        else:
            return "Obesitas"
    elif 60 < umur_bulan <= 216:  # Umur 6-18 tahun
        # Tentukan kategori stanting sesuai dengan standar pertumbuhan anak usia 6-18 tahun
        # Anda dapat menambahkan kriteria sesuai dengan standar yang sesuai dengan sumber Anda.
        # Misalnya, CDC (Centers for Disease Control and Prevention) memiliki standar pertumbuhan anak.
        # Ini hanya contoh sederhana.
        return "Kategori Sesuai Umur 6-18 Tahun"
    else:
        return "Umur di luar jangkauan"

# Contoh penggunaan
umur = 60  # Umur dalam bulan (5 tahun)
tinggi_badan = 110  # Tinggi badan dalam cm
berat_badan = 18  # Berat badan dalam kg

bmi_anak = hitung_bmi(berat_badan, tinggi_badan)
kategori_stanting = tentukan_kategori_stanting(umur, bmi_anak)

print(f"Umur: {umur} bulan")
print(f"Berat Badan: {berat_badan} kg")
print(f"Tinggi Badan: {tinggi_badan} cm")
print(f"BMI: {bmi_anak:.2f}")
print(f"Kategori Stanting: {kategori_stanting}")
