"""
1314. 矩阵区域和
给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和：

i - K <= r <= i + K, j - K <= c <= j + K
(r, c) 在矩阵内。


示例 1：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
示例 2：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]


提示：

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
"""
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + mat[i][j]

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                up = max(0, i - K)
                down = min(m - 1, i + K)
                left = max(0, j - K)
                right = min(n - 1, j + K)
                res[i][j] = pre[down + 1][right + 1] - pre[down + 1][left] - pre[up][right + 1] + pre[up][left]
        return res