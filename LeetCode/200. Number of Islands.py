'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        执行用时 :116 ms, 在所有 Python3 提交中击败了77.32%的用户
        内存消耗 :14.4 MB, 在所有 Python3 提交中击败了19.19%的用户
        :param grid:
        :return:
        '''
        if len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        loc = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != "1":
                return 0
            # 如果为1，记录1，并将值赋值为0
            count = 1
            grid[i][j] = 0
            for k in loc:
                count += dfs(i + k[0], j + k[1])

            return count

        maxValue = 0
        for i in range(row):
            for j in range(col):
                if dfs(i, j) >= 1:
                    maxValue += 1

        return maxValue

    def numIslands2(self, grid: List[List[str]]) -> int:
        '''
        执行用时 :120 ms, 在所有 Python3 提交中击败了47.86%的用户
        内存消耗 :14.4 MB, 在所有 Python3 提交中击败了6.67%的用户
        思路：dfs，从四个方向遍历，将所有1置为0
        :param grid:
        :return:
        '''
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])

        dic = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(i, j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for d in dic:
                if 0 <= i + d[0] < n and 0 <= j + d[1] < m:
                    dfs(i + d[0], j + d[1])

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
                    # print(grid)

        return count

    def numIslands3(self, grid: List[List[str]]) -> int:
        '''
        执行用时 :72 ms, 在所有 Python3 提交中击败了90.79%的用户
        内存消耗 :14.2 MB, 在所有 Python3 提交中击败了6.67%的用户
        思路：这里需要注意，每次将下标加进去的时候，将该位置上的值置为零
        :param grid:
        :return:
        '''
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        dic = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        queue = collections.deque()

        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1':
                    count += 1
                    queue.append((r, c))
                    grid[r][c] = '0'
                    while queue:
                        x, y = queue.popleft()
                        for d in dic:
                            if 0 <= x + d[0] < n and 0 <= y + d[1] < m and grid[x + d[0]][y + d[1]] == '1':
                                queue.append((x + d[0], y + d[1]))
                                grid[x + d[0]][y + d[1]] = '0'

        return count


if __name__ == '__main__':
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    s = Solution()
    print(s.numIslands3(grid))
