"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

 

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

 

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List



class Solution:
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        """
        思路：动态规划法
        1. 在纸上画出图形就好理解了
        1           1
        2 3   ->    3 4
        4 5 6       7 8 10
        """

        n = len(triangle)
        dp = [[0] * (n) for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        return min(dp[-1])

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [float('inf')] * n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i, -1, -1):
                if j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                elif j == i:
                    dp[j] = dp[j - 1] + triangle[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]

        return min(dp)


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(Solution().minimumTotal1(triangle))
    print(Solution().minimumTotal2(triangle))
