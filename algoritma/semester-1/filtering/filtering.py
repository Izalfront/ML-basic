import hashlib
from datetime import datetime

# Simulasi database
data_anak = {}

def generate_kode_unik(nik, nama):
    unique_str = nik.strip() + nama.strip().lower()
    kode = hashlib.sha256(unique_str.encode()).hexdigest()[:10]
    return kode

def admin_input_data():
    print("\n--- Input Data Anak (ADMIN) ---")
    kode_input = input("Masukkan Kode Unik Anak (opsional, tekan Enter jika anak baru): ").strip()

    # Jika data di id unik ada maka jalankan dibawah ini
    if kode_input and kode_input in data_anak:
        print(f"\n🔄 Data anak ditemukan: {data_anak[kode_input]['Nama']} (NIK: {data_anak[kode_input]['NIK']})")
        umur = input("Masukkan Umur (bulan): ")
        berat = input("Masukkan Berat Badan (kg): ")
        tinggi = input("Masukkan Tinggi Badan (cm): ")
        # Tambah ke dalam array riwayat: tanggal, umur, berat, tinggi
        data_anak[kode_input]['Riwayat'].append({
            'Tanggal': datetime.now().strftime('%Y-%m-%d'),
            'Umur': int(umur),
            'Berat': float(berat),
            'Tinggi': float(tinggi)
        })

        print("\n✅ Data pertumbuhan anak berhasil ditambahkan.")
        print(f"🔑 Kode Unik Anak: {kode_input}")

    # Jika data dari id unik tidak ada maka jalankan dibawah ini
    else:
        nik = input("Masukkan NIK Anak: ")
        nama = input("Masukkan Nama Anak: ")
        umur = input("Masukkan Umur (bulan): ")
        berat = input("Masukkan Berat Badan (kg): ")
        tinggi = input("Masukkan Tinggi Badan (cm): ")

        kode = generate_kode_unik(nik, nama)
        if kode not in data_anak:
            data_anak[kode] = {
                'id': kode,
                'NIK': nik,
                'Nama': nama,
                'Riwayat': []
            }

        # Tambah ke dalam array riwayat: tanggal, umur, berat, tinggi
        data_anak[kode]['Riwayat'].append({
            'Tanggal': datetime.now().strftime('%Y-%m-%d'),
            'Umur': int(umur),
            'Berat': float(berat),
            'Tinggi': float(tinggi)
        })

        print("\n✅ Data anak berhasil disimpan.")
        print(f"🔑 Kode Unik Anak (berikan ke ibu): {kode}")

# function lihat data untuk ibu dengan id unik/QRCODE
def ibu_lihat_data():
    print("\n--- Lihat Data Anak (IBU) ---")
    kode = input("Masukkan Kode Unik Anak: ").strip()

    if kode in data_anak:
        anak = data_anak[kode]
        print(f"\n📄 Data Anak:")
        print(f"ID : {anak['id']}")
        print(f"Nama : {anak['Nama']}")
        print(f"NIK  : {anak['NIK']}")
        print("📊 Riwayat Pertumbuhan:")
        sorted_riwayat = sorted(anak['Riwayat'], key=lambda x: x['Umur'])  # urutkan berdasarkan umur

        for idx, r in enumerate(sorted_riwayat, 1):
            print(f"  #{idx} - Tanggal: {r['Tanggal']}, Umur: {r['Umur']} bln, Berat: {r['Berat']} kg, Tinggi: {r['Tinggi']} cm")

        # Tampilkan grafik simulasi berat badan per bulan
        print("\n📈 Grafik Berat Badan per Bulan (simulasi):")
        for r in sorted_riwayat:
            bintang = '*' * int(r['Berat'])
            print(f"Usia {r['Umur']} bln: {bintang} ({r['Berat']} kg)")
    else:
        print("❌ Kode tidak ditemukan.")

# filter data stunting bulan ini hanya menampilkan balita stunting di bulan ini
def filter_stunting_bulan_ini():
    print("\n--- Filter Anak dengan Risiko Stunting (1 Bulan Terakhir) ---")
    bulan_ini = datetime.now().strftime('%Y-%m')

    hasil = []
    for kode, anak in data_anak.items():
        for r in anak['Riwayat']:
            if r['Tanggal'].startswith(bulan_ini):
                # Simulasi logika stunting (sangat sederhana): berat < 8 dan umur >= 6 bulan
                if r['Berat'] < 8 and r['Umur'] >= 6:
                    hasil.append({
                        'ID': anak['id'],
                        'Nama': anak['Nama'],
                        'NIK': anak['NIK'],
                        'Tanggal': r['Tanggal'],
                        'Umur': r['Umur'],
                        'Berat': r['Berat'],
                        'Tinggi': r['Tinggi']
                    })
                    break  # hanya satu entri per anak untuk bulan ini

    if not hasil:
        print("✅ Tidak ditemukan anak dengan risiko stunting dari input bulan ini.")

    # Tampilkan data stunting bulan ini 
    else:
        print("\n📤 Data Anak Risiko Stunting Bulan Ini:")
        for idx, item in enumerate(hasil, 1):
            print(f"\n#{idx}")
            print(f"ID    : {item['ID']}")
            print(f"Nama    : {item['Nama']}")
            print(f"NIK     : {item['NIK']}")
            print(f"Tanggal : {item['Tanggal']}")
            print(f"Umur    : {item['Umur']} bulan")
            print(f"Berat   : {item['Berat']} kg")
            print(f"Tinggi  : {item['Tinggi']} cm")

# Dashboard utama aplikasi
def main():
    while True:
        print("\n=== Aplikasi Monitoring Anak ===")
        print("1. Input Data Anak (Admin)")
        print("2. Lihat Data Anak (Ibu)")
        print("3. Filter Anak Stunting Bulan Ini")
        print("4. Keluar")
        pilih = input("Pilih menu (1/2/3/4): ").strip()

        if pilih == '1':
            admin_input_data()
        elif pilih == '2':
            ibu_lihat_data()
        elif pilih == '3':
            filter_stunting_bulan_ini()
        elif pilih == '4':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()