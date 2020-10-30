"""
有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。

我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。

如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。

请返回封闭岛屿的数目。

 

示例 1：



输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
示例 2：



输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1
示例 3：

输入：grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
输出：2
 

提示：

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-closed-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    flag = 1

    def closedIsland1(self, grid: List[List[int]]) -> int:
        """
        思路：dfs
        1. 根据题意，只要0出现就边缘就不能构成封闭的岛屿
        2. 根据dfs遍历相连的0，并将其赋值为1，如果其中的0出现在边缘上，标记flag为0
        3. 统计flag为1的个数
        """
        dic = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(x, y):
            grid[x][y] = 1
            if x in {0, m - 1} or y in {0, n - 1}:
                self.flag = 0

            for p in dic:
                a, b = p
                # 下面必须写成x+a和y+b,不能写成x和y，否则边缘上的数据遍历不到
                if 0 <= x + a < m and 0 <= y + b < n and grid[x + a][y + b] == 0:
                    dfs(x + a, y + b)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.flag = 1
                    dfs(i, j)
                    count += self.flag

        return count

    def closedIsland2(self, grid: List[List[int]]) -> int:
        # BFS
        result = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        height, width = len(grid), len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    queue = collections.deque()
                    queue.append((i, j))
                    flag = False
                    while queue:
                        x, y = queue.popleft()
                        if x == 0 or x == height - 1 or y == 0 or y == width - 1:
                            flag = True
                        for a, b in directions:
                            m, n = x + a, y + b
                            if 0 <= m < height and 0 <= n < width and grid[m][n] == 0:
                                grid[m][n] = 1
                                queue.append((m, n))
                    if not flag:
                        result += 1
        return result

    def closedIsland3(self, grid: List[List[int]]) -> int:
        # DFS
        result = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        height, width = len(grid), len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    stack = []
                    stack.append((i, j))
                    flag = False
                    while stack:
                        x, y = stack.pop()
                        if x == 0 or x == height - 1 or y == 0 or y == width - 1:
                            flag = True
                        for a, b in directions:
                            m, n = x + a, y + b
                            if 0 <= m < height and 0 <= n < width and grid[m][n] == 0:
                                grid[m][n] = 1
                                stack.append((m, n))
                    if not flag:
                        result += 1
        return result


if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    print(Solution().closedIsland1(grid))
    print(Solution().closedIsland2(grid))
    print(Solution().closedIsland3(grid))
