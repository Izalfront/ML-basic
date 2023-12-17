import numpy as np

# Fungsi untuk menghitung Z-Score Berat Badan menurut Umur (BB/U)
def calculate_z_score_bb_u(umur_bulan, berat_badan_kg, gender):
    # Data referensi dari WHO untuk BB/U
    if gender == "Laki-Laki":
        L = [0.3487, -0.9516, 0.1624, -0.0415, -0.0708, 0.8734, 0.4145, 0.5392, 0.9931]
        M = [9.4785, 8.5978, 7.9792, 7.4631, 6.7164, 6.0834, 5.4136, 5.1516, 4.7886]
        S = [0.1224, 0.1460, 0.1587, 0.1732, 0.1854, 0.1475, 0.1387, 0.1307, 0.1331]
    else:
        L = [0.1563, -0.4380, 0.0728, -0.1062, 0.0906, 0.4711, 0.1537, 0.1553, 0.3625]
        M = [8.9352, 8.1407, 7.5523, 7.0770, 6.2404, 5.5242, 4.8637, 4.5383, 4.2121]
        S = [0.1174, 0.1246, 0.1262, 0.1308, 0.1369, 0.1151, 0.1257, 0.1335, 0.1153]

    z_scores = []

    for i in range(len(L)):
        X = (berat_badan_kg / M[i]) ** L[i] - 1
        Y = L[i] * S[i]
        Z = X / Y
        z_scores.append(Z)

    return z_scores[umur_bulan]

# Fungsi untuk menghitung Z-Score Tinggi Badan menurut Umur (TB/U)
def calculate_z_score_tb_u(umur_bulan, tinggi_badan_cm, gender):
    # Data referensi dari WHO untuk TB/U
    if gender == "Laki-Laki":
        L = [0.1569, -0.0917, 0.1033, -0.0144, 0.0754, 0.5953, 0.4194, 0.4314, 0.4036]
        M = [9.5277, 8.9278, 8.4099, 7.8844, 7.3297, 6.3404, 5.6694, 5.5945, 5.2539]
        S = [0.0827, 0.1134, 0.1259, 0.1305, 0.1354, 0.0979, 0.1187, 0.1097, 0.1070]
    else:
        L = [0.2474, 0.0343, 0.0739, 0.1232, 0.0817, 0.1291, 0.1384, 0.1338, 0.0947]
        M = [9.4607, 8.6674, 8.1877, 7.6733, 7.0814, 6.4387, 5.9322, 5.6602, 5.0677]
        S = [0.0915, 0.1111, 0.1191, 0.1233, 0.1165, 0.1239, 0.1243, 0.1194, 0.1050]

    z_scores = []

    for i in range(len(L)):
        X = (tinggi_badan_cm / M[i]) ** L[i] - 1
        Y = L[i] * S[i]
        Z = X / Y
        z_scores.append(Z)

    return z_scores[umur_bulan]

# Fungsi untuk menghitung Z-Score Berat Badan menurut Tinggi Badan (BB/TB)
def calculate_z_score_bb_tb(tinggi_badan_cm, berat_badan_kg, gender):
    # Data referensi dari WHO untuk BB/TB
    if gender == "Laki-Laki":
        L = [0.8975, 1.4300, -0.4145, 0.6632, 0.4755, 1.4523, 1.7198, 0.8951, 1.0427]
        M = [65.8730, 64.4483, 59.1082, 51.8855, 48.7955, 38.9575, 33.9675, 25.8675, 21.1667]
        S = [13.1520, 12.2040, 11.7700, 11.5450, 11.3880, 10.5920, 10.0650, 9.2300, 8.4910]
    else:
        L = [0.4231, 1.2692, 0.1590, 0.9194, 0.9339, 0.7713, 0.6708, 0.4604, 0.2194]
        M = [61.8997, 60.5119, 56.4415, 51.8154, 49.0955, 43.1056, 37.6950, 29.1475, 24.3611]
        S = [13.9652, 13.2120, 12.7380, 12.5790, 12.3170, 11.5450, 11.0100, 10.4630, 9.4870]

    z_scores = []

    for i in range(len(L)):
        X = (berat_badan_kg / M[i]) ** L[i] - 1
        Y = L[i] * S[i]
        Z = X / Y
        z_scores.append(Z)

    return z_scores

# Fungsi untuk menghitung Z-Score Indeks Massa Tubuh menurut Umur (IMT/U)
def calculate_z_score_imt_u(umur_bulan, bmi, gender):
    # Data referensi dari WHO untuk IMT/U
   
