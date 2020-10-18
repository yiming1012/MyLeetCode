"""
给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。

如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1。

 

示例 1：

输入：
grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1
输出：6
解释：
不消除任何障碍的最短路径是 10。
消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

示例 2：

输入：
grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1
输出：-1
解释：
我们至少需要消除两个障碍才能找到这样的路径。
 

提示：

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-path-in-a-grid-with-obstacles-elimination
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        思路：BFS
        1. 三维数据存储（x,y,rest）坐标和剩余次数
        @param grid:
        @param k:
        @return:
        """
        m, n = len(grid), len(grid[0])
        pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = collections.deque()
        queue.append((0, 0, 0, k))
        visited = set((0, 0, k))
        while queue:
            x, y, steps, rest = queue.popleft()
            if x == m - 1 and y == n - 1 and rest >= 0:
                return steps
            for dx, dy in pos:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < m and 0 <= new_y < n:
                    if grid[new_x][new_y] == 0 and (new_x, new_y, rest) not in visited:
                        queue.append((new_x, new_y, steps + 1, rest))
                        visited.add((new_x, new_y, rest))
                    elif grid[new_x][new_y] == 1 and rest > 0 and (new_x, new_y, rest - 1) not in visited:
                        queue.append((new_x, new_y, steps + 1, rest - 1))
                        visited.add((new_x, new_y, rest - 1))
        return -1


if __name__ == '__main__':
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
    k = 1
    print(Solution().shortestPath(grid, k))
