"""
给你一个大小为 rows x cols 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。

在从左上角 (0, 0) 开始到右下角 (rows - 1, cols - 1) 结束的所有路径中，找出具有 最大非负积 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。

返回 最大非负积 对 109 + 7 取余 的结果。如果最大积为负数，则返回 -1 。

注意，取余是在得到最大积之后执行的。

 

示例 1：

输入：grid = [[-1,-2,-3],
             [-2,-3,-3],
             [-3,-3,-2]]
输出：-1
解释：从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1
示例 2：

输入：grid = [[1,-2,1],
             [1,-2,1],
             [3,-4,1]]
输出：8
解释：最大非负积对应的路径已经用粗体标出 (1 * 1 * -2 * -4 * 1 = 8)
示例 3：

输入：grid = [[1, 3],
             [0,-4]]
输出：0
解释：最大非负积对应的路径已经用粗体标出 (1 * 0 * -4 = 0)
示例 4：

输入：grid = [[ 1, 4,4,0],
             [-2, 0,0,1],
             [ 1,-1,1,1]]
输出：2
解释：最大非负积对应的路径已经用粗体标出 (1 * -2 * 1 * -1 * 1 * 1 = 2)
 

提示：

1 <= rows, cols <= 15
-4 <= grid[i][j] <= 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-non-negative-product-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxProductPath1(self, grid: List[List[int]]) -> int:
        """
        思路：动态规划法
        1. 求乘法最大值，可能出现负数乘上负数变为正数，所以需要同时记录当前的正数最大值和最小值
        @param grid:
        @return:
        """
        mod = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dpmin = [[1] * n for _ in range(m)]
        dpmax = [[1] * n for _ in range(m)]
        dpmin[0][0] = grid[0][0]
        dpmax[0][0] = grid[0][0]
        for i in range(1, m):
            dpmin[i][0] = dpmin[i - 1][0] * grid[i][0]
            dpmax[i][0] = dpmax[i - 1][0] * grid[i][0]
        for j in range(1, n):
            dpmin[0][j] = dpmin[0][j - 1] * grid[0][j]
            dpmax[0][j] = dpmax[0][j - 1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dpmin[i][j] = min(dpmin[i - 1][j] * grid[i][j], dpmax[i - 1][j] * grid[i][j],
                                  dpmin[i][j - 1] * grid[i][j], dpmax[i][j - 1] * grid[i][j])
                dpmax[i][j] = max(dpmin[i - 1][j] * grid[i][j], dpmax[i - 1][j] * grid[i][j],
                                  dpmin[i][j - 1] * grid[i][j], dpmax[i][j - 1] * grid[i][j])

        return dpmax[-1][-1] % mod if dpmax[-1][-1] >= 0 else -1

    def maxProductPath2(self, grid: List[List[int]]) -> int:
        """
        思路：dfs超时
        @param grid:
        @return:
        """
        mod = 10 ** 9 + 7
        res = float('-inf')
        pos = [(1, 0), (0, 1)]
        m, n = len(grid), len(grid[0])

        def dfs(i, j, pre):
            # print(pre)
            nonlocal res
            if pre == 0:
                res = max(res, 0)
                return
            if i == m - 1 and j == n - 1:
                res = max(res, pre)
                # print(res)
                return

            for x, y in pos:
                ix = i + x
                jy = j + y
                if 0 <= ix < m and 0 <= jy < n:
                    dfs(ix, jy, pre * grid[ix][jy])

        dfs(0, 0, grid[0][0])
        return res % mod if res >= 0 else -1


if __name__ == '__main__':
    grid = [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]
    print(Solution().maxProductPath1(grid))
    print(Solution().maxProductPath2(grid))
