# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# Output: 3
# gas mulai dari 0
# 4 - 1 = 3 + 5 = 8
# 8 - 2 = 6 + 1 = 7
# 7 - 3 = 4 + 2 = 6
# 6 - 4 = 2 + 3 = 5
# 5 - 5 = 0 + 4 = 4
# gas = 5 dengan satu keliling
# gas[i] - cost[i] = gas[i] + gas[i+1]
# gas[i+1] - cost[i+1] = gas[i+1] + gas[i+2]
# gas[i+2] - cost[i+2] = gas[i+2] + gas[i+3]
# if gas[i] - cost[i] < 0:
#     gas[i] = 0
# else:
#     gas[i] + gas[i+1]

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
tank = 0
start = 3
n = len(gas)
success = True

for i in range(n):
    idx = (start + i) % n
    tank += gas[idx]
    tank -= cost[idx]
    if tank < 0:
        success = False
        break

if success:
    print("Bisa mulai dari stasiun:", start)
else:
    print("Tidak bisa keliling dari stasiun:", start)