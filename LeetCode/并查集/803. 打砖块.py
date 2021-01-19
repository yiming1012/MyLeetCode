"""
803. 打砖块
有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：

一块砖直接连接到网格的顶部，或者
至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。

返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。

注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。

 

示例 1：

输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
输出：[2]
解释：
网格开始为：
[[1,0,0,0]，
 [1,1,1,0]]
消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0]
 [0,1,1,0]]
两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
[[1,0,0,0],
 [0,0,0,0]]
因此，结果为 [2] 。
示例 2：

输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
输出：[0,0]
解释：
网格开始为：
[[1,0,0,0],
 [1,1,0,0]]
消除 (1,1) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [1,0,0,0]]
剩下的砖都很稳定，所以不会掉落。网格保持不变：
[[1,0,0,0],
 [1,0,0,0]]
接下来消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [0,0,0,0]]
剩下的砖块仍然是稳定的，所以不会有砖块掉落。
因此，结果为 [0,0] 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] 为 0 或 1
1 <= hits.length <= 4 * 104
hits[i].length == 2
0 <= xi <= m - 1
0 <= yi <= n - 1
所有 (xi, yi) 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bricks-falling-when-hit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        length = m * n
        parent = list(range(length + 1))
        size = [1] * (length + 1)
        pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        grid_bak = [arr[:] for arr in grid]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            x, y = find(a), find(b)
            if x != y:
                parent[y] = x
                size[x] += size[y]

        for x, y in hits:
            grid[x][y] = 0

        for i in range(n):
            if grid[0][i] == 1:
                union(i, length)

        for i in range(1, m):
            for j in range(n):
                if grid[i][j] == 1:
                    if grid[i - 1][j] == 1:
                        union((i - 1) * n + j, i * n + j)
                    if j > 0 and grid[i][j - 1] == 1:
                        union(i * n + j, i * n + j - 1)

        # 补砖块
        res = []
        for x, y in hits[::-1]:
            if grid_bak[x][y] == 0:
                res.append(0)
                continue
            pre = size[find(length)]
            if x == 0:
                union(y, length)

            for dx, dy in pos:
                xx, yy = x + dx, y + dy
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1:
                    union(x * n + y, xx * n + yy)

            cur = size[find(length)]
            res.append(max(0, cur - pre - 1))
            grid[x][y] = 1
        return res[::-1]


if __name__ == '__main__':
    grid = [[1, 0, 0, 0], [1, 1, 1, 0]]
    hits = [[1, 0]]
    print(Solution().hitBricks(grid, hits))
