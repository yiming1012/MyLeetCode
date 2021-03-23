"""
5695. N 次操作后的最大分数和
给你 nums ，它是一个大小为 2 * n 的正整数数组。你必须对这个数组执行 n 次操作。

在第 i 次操作时（操作编号从 1 开始），你需要：

选择两个元素 x 和 y 。
获得分数 i * gcd(x, y) 。
将 x 和 y 从 nums 中删除。
请你返回 n 次操作后你能获得的分数和最大为多少。

函数 gcd(x, y) 是 x 和 y 的最大公约数。



示例 1：

输入：nums = [1,2]
输出：1
解释：最优操作是：
(1 * gcd(1, 2)) = 1
示例 2：

输入：nums = [3,4,6,8]
输出：11
解释：最优操作是：
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
示例 3：

输入：nums = [1,2,3,4,5,6]
输出：14
解释：最优操作是：
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14


提示：

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106
"""
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def GCD(a, b):
            if b == 0: return a
            return GCD(b, a % b)

        def bit_count(x):
            count = 0
            while x:
                count += 1
                x &= x - 1
            return count

        n = len(nums)
        dp = [0] * (1 << n)
        for i in range(1 << n):
            cnt = bit_count(i)
            if cnt & 1: continue
            for j in range(n):
                if i >> j & 1:
                    for k in range(n):
                        if (i - (1 << j)) >> k & 1:
                            dp[i] = max(dp[i], dp[i - (1 << j) - (1 << k)] + GCD(nums[j], nums[k]) * cnt // 2)
        return dp[-1]


if __name__ == '__main__':
    nums = [3, 4, 6, 8]
    print(Solution().maxScore(nums))
