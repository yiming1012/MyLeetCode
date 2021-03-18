"""
827. 最大人工岛
在二维地图上， 0代表海洋， 1代表陆地，我们最多只能将一格 0 海洋变成 1变成陆地。

进行填海之后，地图上最大的岛屿面积是多少？（上、下、左、右四个方向相连的 1 可形成岛屿）

示例 1:

输入: [[1, 0], [0, 1]]
输出: 3
解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
示例 2:

输入: [[1, 1], [1, 0]]
输出: 4
解释: 将一格0变成1，岛屿的面积扩大为 4。
示例 3:

输入: [[1, 1], [1, 1]]
输出: 4
解释: 没有0可以让我们变成1，面积依然为 4。
说明:

1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/making-a-large-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        思路：
        1. 获取每个一个连通块，并将该连通块编号，记录每个连通块中连通分量的个数
        2. 遍历每一个为0（海洋）的四周，判断是否存在连通块，有则累加不同的连通块的数量
        @param grid:
        @return:
        """
        m, n = len(grid), len(grid[0])
        matrix = [[0] * n for _ in range(m)]
        pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def dfs(x, y):
            visited.add((x, y))
            matrix[x][y] = index
            cnt = 1
            for dx, dy in pos:
                xx, yy = x + dx, y + dy
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1 and (xx, yy) not in visited:
                    cnt += dfs(xx, yy)
            return cnt

        index = 1
        dic = {}
        ans = 0
        nums = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    nums.append((i, j))
                    continue
                if grid[i][j] == 1 and (i, j) not in visited:
                    cnt = dfs(i, j)
                    ans = max(ans, cnt)
                    dic[index] = cnt
                    index += 1

        res = ans
        for i, j in nums:
            used = set()
            cnt = 1
            for dx, dy in pos:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > 0 and matrix[x][y] not in used:
                    used.add(matrix[x][y])
                    cnt += dic[matrix[x][y]]
            res = max(res, cnt)
        return res


if __name__ == '__main__':
    grid = [[1, 0], [0, 1]]
    print(Solution().largestIsland(grid))
