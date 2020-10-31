'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

'''
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        执行用时 :96 ms, 在所有 Python3 提交中击败了12.57%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了17.24%的用户
        :param grid:
        :return:
        '''
        m, n, time = len(grid), len(grid[0]), 0
        queue = []
        location = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, time))

        while queue:
            loc_i, loc_j, time = queue.pop(0)
            for loc in location:
                i = loc_i + loc[0]
                j = loc_j + loc[1]
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    grid[i][j] = 2
                    queue.append((i, j, time + 1))

        for i in range(m):
            if 1 in grid[i]:
                return -1

        return time

    def orangesRotting2(self, grid: List[List[int]]) -> int:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了87.72%的用户
        内存消耗 :13.3 MB, 在所有 Python3 提交中击败了17.24%的用户
        :param grid:
        :return:
        '''
        m, n, time = len(grid), len(grid[0]), 0
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, time))

        while queue:
            i, j, time = queue.pop(0)

            if 0 <= i - 1 and grid[i - 1][j] == 1:
                grid[i - 1][j] = 2
                queue.append((i - 1, j, time + 1))
            if i + 1 < m and grid[i + 1][j] == 1:
                grid[i + 1][j] = 2
                queue.append((i + 1, j, time + 1))
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                grid[i][j - 1] = 2
                queue.append((i, j - 1, time + 1))
            if j + 1 < n and grid[i][j + 1] == 1:
                grid[i][j + 1] = 2
                queue.append((i, j + 1, time + 1))

        for i in range(m):
            if 1 in grid[i]:
                return -1

        return time

'''
这是一道BFS的题。一般涉及到一层层去传递，都会考虑到用队列或数组
思路：首先遍历找到所有腐烂的橘子，将每个橘子加到队列，每次弹出一个对其相邻的点分析，如果为1，则将其加入到队列，time+1
当队列为空，说明所有腐烂的橘子都将临近的腐烂了
遍历整个数组，看是否存在正常橘子，存在则输出-1，不存在则输出time

复杂度分析
1、时间复杂度：O(nm)O(nm)
即进行一次广度优先搜索的时间，其中 n=grid.lengthn=grid.length, m=grid[0].lengthm=grid[0].length 。

2、空间复杂度：O(nm)O(nm)
需要额外的 disdis 数组记录每个新鲜橘子被腐烂的最短时间，大小为 O(nm)O(nm)，且广度优先搜索中队列里存放的状态最多不会超过 nmnm 个，最多需要 O(nm)O(nm) 的空间，所以最后的空间复杂度为 O(nm)O(nm)。


'''


grid1 = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[0,2]]
grid3 = [[2,1,1],[0,1,1],[1,0,1]]
s = Solution()
print(s.orangesRotting(grid3))