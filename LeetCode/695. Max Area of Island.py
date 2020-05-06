'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        执行用时 :164 ms, 在所有 Python3 提交中击败了58.71%的用户
        内存消耗 :16.4 MB, 在所有 Python3 提交中击败了8.34%的用户
        :param grid: 
        :return:
        '''
        if len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        loc = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != 1:
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
                maxValue = max(dfs(i, j), maxValue)

        return maxValue






