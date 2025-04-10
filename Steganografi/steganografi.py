from PIL import Image

def encode_message(image_path, message, output_path):
    # Buka gambar
    img = Image.open(image_path)
    width, height = img.size

    # Konversi pesan ke dalam bentuk biner
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    message_length = len(binary_message)

    # Periksa apakah pesan bisa dimasukkan ke dalam gambar
    if message_length > width * height * 3:
        raise ValueError("Pesan terlalu panjang untuk dimasukkan ke dalam gambar ini.")

    # Sisipkan pesan ke dalam gambar
    index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))

            for i in range(3):  # RGB
                if index < message_length:
                    pixel[i] = pixel[i] & ~1 | int(binary_message[index])
                    index += 1

            img.putpixel((x, y), tuple(pixel))

    # Simpan gambar yang telah dimodifikasi
    img.save(output_path)
    print(f"Pesan berhasil disisipkan ke dalam gambar dan disimpan sebagai {output_path}")

def decode_message(image_path):
    # Buka gambar
    img = Image.open(image_path)
    width, height = img.size

    # Ekstrak pesan dari gambar
    binary_message = ""
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))

            for i in range(3):  # RGB
                binary_message += str(pixel[i] & 1)

    # Konversi biner ke teks
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
        if message[-1] == '\0':  # Karakter null menandakan akhir pesan
            break

    return message

# Contoh penggunaan
image_path = "81418926_9890005.jpg"
output_path = "81418926_9890004.png"
message = "Masih gagal move on"

# Encode pesan ke dalam gambar
encode_message(image_path, message, output_path)

# Decode pesan dari gambar
decoded_message = decode_message(output_path)
print(f"Pesan yang di-decode: {decoded_message}")