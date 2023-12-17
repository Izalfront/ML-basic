# Dictionary untuk standar status gizi
standar_status_gizi = {
    "Laki-Laki": {
        "0-5_BeratBadanUmur": {
            (0, 24): (-3, -2, -1, 0, 1, 2, 3),
            (24, 60): (-3, -2, -1, 0, 1, 2, 3)
        },
        "0-5_TinggiBadanUmur": {
            (0, 24): (-3, -2, -1, 0, 1, 2, 3),
            (24, 60): (-3, -2, -1, 0, 1, 2, 3)
        },
        "0-24_BeratBadanPanjangBadan": (-3, -2, -1, 0, 1, 2, 3),
        "24-60_BeratBadanTinggiBadan": (-3, -2, -1, 0, 1, 2, 3),
        "5-18_IMTUmur": (-3, -2, -1, 0, 1, 2, 3)
    },
    "Perempuan": {
        "0-5_BeratBadanUmur": {
            (0, 24): (-3, -2, -1, 0, 1, 2, 3),
            (24, 60): (-3, -2, -1, 0, 1, 2, 3)
        },
        "0-5_TinggiBadanUmur": {
            (0, 24): (-3, -2, -1, 0, 1, 2, 3),
            (24, 60): (-3, -2, -1, 0, 1, 2, 3)
        },
        "0-24_BeratBadanPanjangBadan": (-3, -2, -1, 0, 1, 2, 3),
        "24-60_BeratBadanTinggiBadan": (-3, -2, -1, 0, 1, 2, 3),
        "5-18_IMTUmur": (-3, -2, -1, 0, 1, 2, 3)
    }
}

# Fungsi untuk menghitung BMI
def calculate_bmi(berat_badan_kg, tinggi_badan_cm):
    tinggi_badan_m = tinggi_badan_cm / 100
    bmi = berat_badan_kg / (tinggi_badan_m * tinggi_badan_m)
    return bmi

# Fungsi untuk menentukan kategori status gizi berdasarkan umur, jenis kelamin, dan parameter
def categorize_gizi_umur(umur_tahun, umur_bulan, berat_badan_kg, tinggi_badan_cm, gender, parameter):
    if umur_tahun < 0 or umur_bulan < 0:
        return "Umur tidak valid"
    
    if gender not in standar_status_gizi:
        return "Jenis kelamin tidak valid"
    
    if parameter not in standar_status_gizi[gender]:
        return "Parameter tidak valid"
    
    kriteria = standar_status_gizi[gender][parameter]
    
    # Menentukan BMI berdasarkan berat badan dan tinggi badan
    bmi = calculate_bmi(berat_badan_kg, tinggi_badan_cm)
    
    # Menentukan kategori status gizi berdasarkan kriteria
    status_gizi = None
    for rentang, kategori in kriteria.items():
        if rentang[0] <= umur_bulan <= rentang[1]:
            if kategori[0] <= bmi < kategori[-1]:
                status_gizi = kategori
                break
    
    return bmi, status_gizi

# Contoh penggunaan
umur_tahun = 5  # Ganti dengan umur dalam tahun
umur_bulan = 6  # Ganti dengan umur dalam bulan
berat_badan = 15  # Ganti dengan berat badan yang sesuai
tinggi_badan = 90  # Ganti dengan tinggi badan yang sesuai
gender = "Laki-Laki"  # Ganti dengan "Laki-Laki" atau "Perempuan" sesuai gender
parameter = "0-5_BeratBadanUmur"  # Ganti dengan parameter yang sesuai

bmi, status_gizi = categorize_gizi_umur(umur_tahun, umur_bulan, berat_badan, tinggi_badan, gender, parameter)

print(f"Umur: {umur_tahun} tahun {umur_bulan} bulan")
print(f"Gender: {gender}")
print(f"Berat Badan: {berat_badan} kg")
print(f"Tinggi Badan: {tinggi_badan} cm")
print(f"BMI: {bmi}")
if status_gizi is not None:
    print(f"Status Gizi: {status_gizi}")
