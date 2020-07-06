"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maximalRectangle1(self, mat: List[List[str]]) -> int:
        """
        思路：动态规划法
        1. 从左到右计算连续1的个数
        2. 从下到上计算每种宽度矩形的面积(i - k + 1) * minN
        """
        if not mat:
            return 0
        m, n = len(mat), len(mat[0])
        res = 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == "1":
                    dp[i][j] = dp[i][j - 1] + 1 if j > 0 else 1
                    minN = float('inf')
                    for k in range(i, -1, -1):
                        if dp[k][j]:
                            minN = min(minN, dp[k][j])
                            res = max(res, (i - k + 1) * minN)
                            # print(res)
                        else:
                            break
        return res

    def maximalRectangle2(self, matrix: List[List[str]]) -> int:
        """
        思路：前缀和+单调栈
        1. 计算每一列前面连续1的个数，即每个矩形的高度
        2. 每一行利用单调栈计算最大的矩形
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = dp[i - 1][j] + 1 if i > 0 else 1
            stack = [-1]
            nums = dp[i]
            nums.append(0)
            for k, num in enumerate(nums):
                while stack and nums[stack[-1]] > num:
                    index = stack.pop()
                    res = max(res, (k - stack[-1] - 1) * nums[index])
                stack.append(k)

        return res


if __name__ == '__main__':
    matric = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(Solution().maximalRectangle1(matric))
    print(Solution().maximalRectangle2(matric))
