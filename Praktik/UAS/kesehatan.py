import math
import operator

# Data gejala dan penyakit (Contoh data sederhana, bisa ditambahkan lebih banyak data)
data_training = {
    'P1': [1, 1, 0, 1, 'Flu'],
    'P2': [1, 0, 1, 0, 'Flu'],
    'P3': [0, 1, 0, 1, 'Cold'],
    'P4': [0, 1, 1, 0, 'Cold'],
}

def euclidean_distance(instance1, instance2):
    distance = 0
    for i in range(len(instance1) - 1):
        distance += pow((instance1[i] - instance2[i]), 2)
    return math.sqrt(distance)

def get_neighbors(training_set, test_instance, k):
    distances = []
    for key in training_set:
        dist = euclidean_distance(test_instance, training_set[key])
        distances.append((key, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors

def get_response(neighbors, training_set):
    class_votes = {}
    for neighbor in neighbors:
        response = training_set[neighbor][-1]
        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1
    sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]

# Input gejala dari pengguna
input_gejala = [1, 0, 0, 1]

# Jumlah tetangga terdekat yang akan dipertimbangkan
k = 3

# Proses diagnosa
neighbors = get_neighbors(data_training, input_gejala, k)
result = get_response(neighbors, data_training)

print(f"Gejala yang dimasukkan: {input_gejala}")
print(f"Hasil diagnosa: {result}")
