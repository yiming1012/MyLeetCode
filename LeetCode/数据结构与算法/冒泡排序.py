nums = [2, 1, 3, 5, 4]
for i in range(len(nums) - 1, -1, -1):
    flag = 0
    for j in range(1, i + 1):
        if nums[j - 1] > nums[j]:
            flag = 1
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
    if flag == 0:
        break
    print(nums)
print(nums)
