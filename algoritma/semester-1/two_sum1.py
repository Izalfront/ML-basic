def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Contoh penggunaan
nums = [1, 8, 11, 15]
target = 9
print("Brute Force:", two_sum_brute_force(nums, target))
