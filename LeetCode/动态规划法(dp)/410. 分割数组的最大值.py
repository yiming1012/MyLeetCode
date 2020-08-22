"""
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-largest-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        思路:动态规划法
        1. dp[i][j]:表示前i个数划分为j段和的最大值的最小值
        2. 每次遍历，计算前k个数划分为j-i段，与后面k到i段的总和的大小，即pre[i]-pre[k]，两者取最大值
        3. 上面的值与dp[i][j]求最小值
        注：上面第二步其实是松弛的过程，找到前面i个数划分为j段的最优解，通过k来松弛

        """
        n = len(nums)
        pre = [0] + nums
        for i in range(1, n + 1):
            pre[i] += pre[i - 1]

        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = pre[i]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], pre[i] - pre[k]))
        return dp[-1][-1]


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    print(Solution().splitArray(nums, m))

