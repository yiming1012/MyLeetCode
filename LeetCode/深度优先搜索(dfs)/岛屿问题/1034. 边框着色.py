"""
给出一个二维整数网格 grid，网格中的每个值表示该位置处的网格块的颜色。

只有当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一连通分量。

连通分量的边界是指连通分量中的所有与不在分量中的正方形相邻（四个方向上）的所有正方形，或者在网格的边界上（第一行/列或最后一行/列）的所有正方形。

给出位于 (r0, c0) 的网格块和颜色 color，使用指定颜色 color 为所给网格块的连通分量的边界进行着色，并返回最终的网格 grid 。

 

示例 1：

输入：grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
输出：[[3, 3], [3, 2]]
示例 2：

输入：grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
输出：[[1, 3, 3], [2, 3, 3]]
示例 3：

输入：grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
输出：[[2, 2, 2], [2, 1, 2], [2, 2, 2]]
 

提示：

1 <= grid.length <= 50
1 <= grid[0].length <= 50
1 <= grid[i][j] <= 1000
0 <= r0 < grid.length
0 <= c0 < grid[0].length
1 <= color <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coloring-a-border
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        """
        思路：DFS
        1. 和初始点(r0,c0)连通的区域，如果点在边界上或者该点和下一个点不同则染色
        2. 对于已经访问过的点加入标记
        3. 注意判断是否和grid[r0][c0]相同时，需提前存为target，而不能直接判断grid[a][b] == grid[r0][c0]，踩过坑
        @param grid:
        @param r0:
        @param c0:
        @param color:
        @return:
        """
        # 边界条件判断
        if not grid:
            return []

        pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 定义方向
        m, n = len(grid), len(grid[0])
        visited = set()
        visited.add((r0, c0))
        target = grid[r0][c0]

        def dfs(x, y):
            # 判断是否为矩阵边界:着色
            if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                grid[x][y] = color

            # 搜索4个方向
            for i, j in pos:
                a = x + i
                b = y + j

                # 判断是否越界
                if 0 <= a < m and 0 <= b < n:
                    # 判断是否访问过
                    if (a, b) not in visited:
                        # 判断是否为连通量，只要出现非连通量，则当前的位置就是边界
                        if grid[a][b] == target:
                            visited.add((a, b))
                            dfs(a, b)  # 深搜
                        else:
                            # 当前位置是边界，着色
                            grid[x][y] = color

        dfs(r0, c0)  # 寻找连通分量
        return grid


if __name__ == '__main__':
    grid = [[1, 1], [1, 2]]
    r0 = 0
    c0 = 0
    color = 3
    print(Solution().colorBorder(grid, r0, c0, color))
