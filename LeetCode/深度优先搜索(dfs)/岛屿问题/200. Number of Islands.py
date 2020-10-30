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
    def numIslands1(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0

        def dfs(x, y):
            grid[x][y] = "0"
            for i, j in pos:
                a, b = x + i, y + j
                if 0 <= a < m and 0 <= b < n and grid[a][b] == "1":
                    dfs(a, b)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res

    def numIslands2(self, grid: List[List[str]]) -> int:
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
    print(s.numIslands1(grid))
    print(s.numIslands2(grid))
