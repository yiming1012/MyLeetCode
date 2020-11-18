"""
5553. 分配重复整数
给你一个长度为 n 的整数数组 nums ，这个数组中至多有 50 个不同的值。同时你有 m 个顾客的订单 quantity ，其中，整数 quantity[i] 是第 i 位顾客订单的数目。请你判断是否能将 nums 中的整数分配给这些顾客，且满足：

第 i 位顾客 恰好 有 quantity[i] 个整数。
第 i 位顾客拿到的整数都是 相同的 。
每位顾客都满足上述两个要求。
如果你可以分配 nums 中的整数满足上面的要求，那么请返回 true ，否则返回 false 。



示例 1：

输入：nums = [1,2,3,4], quantity = [2]
输出：false
解释：第 0 位顾客没办法得到两个相同的整数。
示例 2：

输入：nums = [1,2,3,3], quantity = [2]
输出：true
解释：第 0 位顾客得到 [3,3] 。整数 [1,2] 都没有被使用。
示例 3：

输入：nums = [1,1,2,2], quantity = [2,2]
输出：true
解释：第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [2,2] 。
示例 4：

输入：nums = [1,1,2,3], quantity = [2,2]
输出：false
解释：尽管第 0 位顾客可以得到 [1,1] ，第 1 位顾客没法得到 2 个一样的整数。
示例 5：

输入：nums = [1,1,1,1,1], quantity = [2,3]
输出：true
解释：第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [1,1,1] 。


提示：

n == nums.length
1 <= n <= 105
1 <= nums[i] <= 1000
m == quantity.length
1 <= m <= 10
1 <= quantity[i] <= 105
nums 中至多有 50 个不同的数字。
"""
import collections
from typing import List


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        cnt = collections.Counter(nums)
        n = len(cnt)
        m = len(quantity)
        # 预处理，计算每个状态需要的个数
        needed = [0] * (1 << m)
        for i in range(m):
            for j in range(1 << m):
                if j >> i & 1:
                    needed[j] += quantity[i]

        dp = [[False] * (1 << m) for _ in range(n + 1)]
        dp[0][0] = True
        for i, v in enumerate(cnt.values()):
            for j in range(1 << m):
                if dp[i][j]:
                    dp[i + 1][j] = True

                    # 计算子集
                    t = j ^ ((1 << m) - 1)
                    sub = t
                    while sub:
                        # 判断当前子集所需个数是否小于等于持有的v
                        if needed[sub] <= v:
                            dp[i + 1][j | sub] = True
                        sub = t & (sub - 1)

        return dp[-1][-1]


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    quantity = [2]
    print(Solution().canDistribute(nums, quantity))
