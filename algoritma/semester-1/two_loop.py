data = [1, 2, 3, 4, 5]
counter = 0

for val in data:
    print(val)
    counter += 1
    if counter == 4:  # batasi hanya 2 kali
        break

print("Ini adalah 2 nilai pertama dari data.")
