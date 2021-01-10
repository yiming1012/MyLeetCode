"""
1210. 穿过迷宫的最少移动次数
你还记得那条风靡全球的贪吃蛇吗？

我们在一个 n*n 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（(0, 0) 和 (0, 1)）开始移动。我们用 0 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（(n-1, n-2) 和 (n-1, n-1)）。

每次移动，蛇可以这样走：

如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。
如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。
如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（(r, c)、(r, c+1)）移动到 （(r, c)、(r+1, c)）。

如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（(r, c)、(r+1, c)）移动到（(r, c)、(r, c+1)）。

返回蛇抵达目的地所需的最少移动次数。

如果无法到达目的地，请返回 -1。



示例 1：



输入：grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
输出：11
解释：
一种可能的解决方案是 [右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。
示例 2：

输入：grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
输出：9


提示：

2 <= n <= 100
0 <= grid[i][j] <= 1
蛇保证从空单元格开始出发。
"""
import collections
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[0][1] == 1 or grid[n - 1][n - 2] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        queue = collections.deque()
        visited = set()
        visited.add((0, 0, 0, 1))
        queue.append((0, 0, 0, 1))
        step = 0
        # 通过横纵坐标是否相等 ，判断蛇的方向
        while queue:
            for _ in range(len(queue)):
                x1, y1, x2, y2 = queue.popleft()
                if (x1, y1, x2, y2) == (n - 1, n - 2, n - 1, n - 1):
                    return step
                # 横着的
                if x1 == x2:
                    # 向右
                    if y2 + 1 < n and grid[x2][y2 + 1] == 0 and (x2, y2, x2, y2 + 1) not in visited:
                        visited.add((x2, y2, x2, y2 + 1))
                        queue.append((x2, y2, x2, y2 + 1))
                    # 向下平移
                    if x1 + 1 < n and grid[x1 + 1][y1] == 0 and grid[x2 + 1][y2] == 0 and (
                            x1 + 1, y1, x2 + 1, y2) not in visited:
                        visited.add((x1 + 1, y1, x2 + 1, y2))
                        queue.append((x1 + 1, y1, x2 + 1, y2))
                    # 顺时针
                    if x1 + 1 < n and grid[x1 + 1][y1] == 0 and grid[x2 + 1][y2] == 0 and (
                            x1, y1, x1 + 1, y1) not in visited:
                        visited.add((x1, y1, x1 + 1, y1))
                        queue.append((x1, y1, x1 + 1, y1))
                if y1 == y2:  # 垂直的
                    # 向下
                    if x2 + 1 < n and grid[x2 + 1][y2] == 0 and (x2, y2, x2 + 1, y2) not in visited:
                        visited.add((x2, y2, x2 + 1, y2))
                        queue.append((x2, y2, x2 + 1, y2))
                    # 向右平移
                    if y1 + 1 < n and grid[x1][y1 + 1] == 0 and grid[x2][y2 + 1] == 0 and (
                            x1, y1 + 1, x2, y2 + 1) not in visited:
                        visited.add((x1, y1 + 1, x2, y2 + 1))
                        queue.append((x1, y1 + 1, x2, y2 + 1))
                    # 向右
                    if y1 + 1 < n and grid[x1][y1 + 1] == 0 and grid[x2][y2 + 1] == 0 and (
                            x1, y1, x1, y1 + 1) not in visited:
                        visited.add((x1, y1, x1, y1 + 1))
                        queue.append((x1, y1, x1, y1 + 1))

            step += 1
        return -1


if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0]]
    print(Solution().minimumMoves(grid))
