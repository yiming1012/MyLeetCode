"""
1631. 最小体力消耗路径
你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。
一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。
你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。

请你返回从左上角走到右下角的最小 体力消耗值 。

 

示例 1：



输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
输出：2
解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
示例 2：



输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
输出：1
解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
示例 3：


输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
输出：0
解释：上图所示路径不需要消耗任何体力。
 

提示：

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-with-minimum-effort
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq
from typing import List


class Solution:
    def minimumEffortPath1(self, heights: List[List[int]]) -> int:
        """
        思路：
        1. 先将相邻两个点的距离存入edge，然后按边权重从小到大排序
        2. 一次合并每条边，如果首尾相连了，说明当前的权重即为所求
        @param heights:
        @return:
        """
        m, n = len(heights), len(heights[0])
        parent = list(range(m * n))
        edge = []

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def unoin(a, b):
            x, y = find(a), find(b)
            if x != y:
                parent[y] = x
                return False
            return True

        for i in range(m):
            for j in range(n):
                pos = i * n + j
                if i < m - 1:
                    edge.append((abs(heights[i][j] - heights[i + 1][j]), pos, pos + n))
                if j < n - 1:
                    edge.append((abs(heights[i][j] - heights[i][j + 1]), pos, pos + 1))

        edge.sort()
        for w, u, v in edge:
            unoin(u, v)
            if find(0) == find(m * n - 1):
                return w
        return 0

    def minimumEffortPath2(self, heights: List[List[int]]) -> int:
        """
        思路：最短路+堆优化
        @param heights:
        @return:
        """
        row, col = len(heights), len(heights[0])
        pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = {(i, j): float('inf') for j in range(col) for i in range(row)}
        dist[(0, 0)] = 0
        pq = [(0, 0, 0)]
        while pq:
            dis, x, y = heapq.heappop(pq)
            for i, j in pos:
                if 0 <= x + i < row and 0 <= y + j < col:
                    new_dis = max(dis, abs(heights[x + i][y + j] - heights[x][y]))
                    if new_dis < dist[(x + i, y + j)]:
                        dist[(x + i, y + j)] = new_dis
                        heapq.heappush(pq, (new_dis, x + i, y + j))
        return dist[(row - 1, col - 1)]


if __name__ == '__main__':
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(Solution().minimumEffortPath1(heights))
    print(Solution().minimumEffortPath2(heights))
