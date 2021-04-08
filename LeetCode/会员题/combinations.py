def dfs(cur, arr):
    res.append(arr.copy())
    for i in range(cur, n):
        dfs(i + 1, arr + [nums[i]])


nums = [1, 2, 3, 3]
n = len(nums)
res = []
dfs(0, [])
print(res)
