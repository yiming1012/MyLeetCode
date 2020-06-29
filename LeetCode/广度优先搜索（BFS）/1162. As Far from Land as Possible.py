'''
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation:
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:



Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation:
The cell (2, 2) is as far as possible from all the land with distance 4.
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
from typing import List


class Solution:
    def maxDistance1(self, grid: List[List[int]]) -> int:
        n = len(grid)
        steps = -1
        queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        if len(queue) == 0 or len(queue) == n ** 2: return steps
        while len(queue) > 0:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for xi, yj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if xi >= 0 and xi < n and yj >= 0 and yj < n and grid[xi][yj] == 0:
                        queue.append((xi, yj))
                        grid[xi][yj] = -1
            steps += 1

        return steps

    def maxDistance2(self, grid: List[List[int]]) -> int:
        """
        思路：多源BFS
        1. 先将满足条件的坐标添加到队列当中，再由近到远遍历，统计计算距离
        """
        pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited.add((i, j))
        queue = collections.deque(visited)
        res = float('-inf')
        while queue:
            x, y = queue.popleft()
            for p in pos:
                a, b = p
                xa, yb = x + a, y + b
                if 0 <= xa < m and 0 <= yb < n and (xa, yb) not in visited:
                    queue.append((xa, yb))
                    visited.add((xa, yb))
                    dp[xa][yb] = dp[x][y] + 1
                    res = max(res, dp[xa][yb])
        return res if res != float('-inf') else -1


if __name__ == '__main__':
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(Solution().maxDistance1(grid))
    print(Solution().maxDistance2(grid))
