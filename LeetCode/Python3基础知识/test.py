nums = [-3, -2, -1, 0, 3, 1, 2]


def sum(nums):
    nums.sort()
    n = len(nums)

    for i in range(n - 2):
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif s > 0:
                r -= 1
            else:
                l += 1


res = []
sum(nums)
print(res)
