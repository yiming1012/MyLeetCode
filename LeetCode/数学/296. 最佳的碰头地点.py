"""
296. 最佳的碰头地点
有一队人（两人或以上）想要在一个地方碰面，他们希望能够最小化他们的总行走距离。

给你一个 2D 网格，其中各个格子内的值要么是 0，要么是 1。

1 表示某个人的家所处的位置。这里，我们将使用 曼哈顿距离 来计算，其中 distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|。

示例：

输入:

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

输出: 6

解析: 给定的三个人分别住在(0,0)，(0,4) 和 (2,2):
     (0,2) 是一个最佳的碰面点，其总行走距离为 2 + 2 + 2 = 6，最小，因此返回 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-meeting-point
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        row, col = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)
        row.sort()
        col.sort()

        def helper(tmp):
            nonlocal res
            l, r = 0, len(tmp) - 1
            while l < r:
                res += tmp[r] - tmp[l]
                l += 1
                r -= 1

        res = 0
        helper(row)
        helper(col)

        return res
