"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]。
说明:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        思路：动态规划法+记录最大值
        1. 要求最长子数组，不同于最长子序列，子数组必须连续
        2. 动态转移方程：dp[i + 1][j + 1] = dp[i][j] + 1
        """
        m = len(A)
        n = len(B)
        res = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                # 只对相等的数进行判断
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    res = max(res, dp[i + 1][j + 1])
        return res


if __name__ == '__main__':
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    print(Solution().findLength(A, B))
