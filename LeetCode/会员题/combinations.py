def subset(arr):
    res.append(arr.copy())
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1] and i - 1 in visited: continue
        if i not in visited:
            visited.add(i)
            subset(arr + [nums[i]])
            visited.remove(i)


def permutations(nums):
    arr = []
    nums.sort()
    visited = set()
    n = len(nums)

    def dfs(tmp):
        if len(tmp) == n:
            arr.append(tmp.copy())
            return
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited:
                continue
            if i not in visited:
                visited.add(i)
                dfs(tmp + [nums[i]])
                visited.remove(i)
        return arr

    dfs([])
    print(arr)
    return arr


def bitmask():
    n = len(nums)
    arr = []
    visited = set()
    for i in range(1 << n):
        arr.clear()
        for j in range(n):
            if i >> j & 1:
                arr.append(nums[j])
        visited.add(tuple(arr))
    return [list(v) for v in visited]


nums = [2, 1, 3, 2]
# nums="abcd"
visited = set()
nums.sort()
n = len(nums)
res = []
subset([])
print(res)
# ans = []
# for arr in res:
#     ans.extend(permutations(arr))
# print(ans)
# print(len(ans))

import math

print(1 + int(math.log10(1001)))
