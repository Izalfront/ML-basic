def find_two_largest(arr):
    if len(arr) < 2:
        return sorted(arr, reverse=True)  # Kembalikan semua jika kurang dari 2 elemen

    largest = float('-inf')  # Inisialisasi dengan nilai negatif tak hingga
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return sorted([largest, second_largest], reverse=True)

# Contoh penggunaan
my_array = [5, 2, 8, 1, 9, 3, 9]
two_largest = find_two_largest(my_array)
print(f"Dua angka terbesar dalam array adalah: {two_largest}")