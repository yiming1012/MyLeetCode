"""
1139. 最大的以 1 为边界的正方形
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。



示例 1：

输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9
示例 2：

输入：grid = [[1,1,0,0]]
输出：1


提示：

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] 为 0 或 1
"""
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        """
        思路：动态规划法
        @param grid:
        @return:
        """
        res = 0
        m, n = len(grid), len(grid[0])
        pre = [[[0] * 2 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    pre[i + 1][j + 1][0] = pre[i + 1][j][0] + 1
                    pre[i + 1][j + 1][1] = pre[i][j + 1][1] + 1

                    for k in range(min(pre[i + 1][j + 1]), 0, -1):
                        if res < k <= pre[i - k + 2][j + 1][0] and pre[i + 1][j - k + 2][1] >= k:
                            res = k

        return res * res


if __name__ == '__main__':
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(Solution().largest1BorderedSquare(grid))
