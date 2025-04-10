from PIL import Image

def analyze_lsb(image_path):
    img = Image.open(image_path)
    width, height = img.size

    # Ekstrak bit terakhir (LSB) dari setiap pixel
    lsb_data = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            lsb_data.extend([pixel[i] & 1 for i in range(3)])  # RGB

    # Hitung frekuensi bit 0 dan 1
    freq_0 = lsb_data.count(0)
    freq_1 = lsb_data.count(1)

    print(f"Frekuensi bit 0: {freq_0}")
    print(f"Frekuensi bit 1: {freq_1}")

    # Jika distribusi bit tidak seimbang, mungkin ada pesan tersembunyi
    if abs(freq_0 - freq_1) > 1000:  # Ambang batas arbitrer
        print("Kemungkinan ada pesan tersembunyi dalam gambar.")
    else:
        print("Tidak ada indikasi pesan tersembunyi.")

# Contoh penggunaan
analyze_lsb("decode.jpeg")