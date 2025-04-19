nums = [-2,1,-3,4,-1,2,1,-5,4]

# Inisialisasi nilai awal
max_so_far = nums[0]
current_sum = nums[0]

for i in range(1, len(nums)):
    # Pilih: lanjutkan dari sebelumnya atau mulai baru (manual dengan if)
    if current_sum + nums[i] > nums[i]:
        current_sum += nums[i]
    else:
        current_sum = nums[i]
        
    # Update nilai maksimum global (manual dengan if)
    if current_sum > max_so_far:
        max_so_far = current_sum

print(max_so_far)
