from PIL import Image

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
        char = chr(int(byte, 2))
        if char == '\0':  # Karakter null menandakan akhir pesan
            break
        message += char
    
    return message

# Contoh penggunaan
image_path = "81418926_9890004.png"
decoded_message = decode_message(image_path)
print(f"Pesan yang di-decode: {decoded_message}")
