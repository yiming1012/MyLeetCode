"""
给你一个奇怪的打印机，它有如下两个特殊的打印规则：

每一次操作时，打印机会用同一种颜色打印一个矩形的形状，每次打印会覆盖矩形对应格子里原本的颜色。
一旦矩形根据上面的规则使用了一种颜色，那么 相同的颜色不能再被使用 。
给你一个初始没有颜色的 m x n 的矩形 targetGrid ，其中 targetGrid[row][col] 是位置 (row, col) 的颜色。

如果你能按照上述规则打印出矩形 targetGrid ，请你返回 true ，否则返回 false 。

 

示例 1：



输入：targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
输出：true
示例 2：



输入：targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
输出：true
示例 3：

输入：targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
输出：false
解释：没有办法得到 targetGrid ，因为每一轮操作使用的颜色互不相同。
示例 4：

输入：targetGrid = [[1,1,1],[3,1,3]]
输出：false
 

提示：

m == targetGrid.length
n == targetGrid[i].length
1 <= m, n <= 60
1 <= targetGrid[row][col] <= 60

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/strange-printer-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import deque
from typing import List


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        """
        思路：拓扑排序
        1. 从小到大遍历每一种颜色，找到每个颜色可以覆盖的最大面积，判断每个颜色是否被其他颜色覆盖
        2. 如果某个颜色被其他颜色覆盖，那么其他颜色的入度+1
        3. 每次计算入度为0的点，判断最后是不是所有点都被访问过
        @param targetGrid:
        @return:
        """

        def build(c, inds):
            x1, y1, x2, y2 = m, n, -1, -1
            for i in range(m):
                for j in range(n):
                    if c == targetGrid[i][j]:
                        x1, y1 = min(x1, i), min(y1, j)
                        x2, y2 = max(x2, i), max(y2, j)

            # print(c, x1, x2, y1, y2)
            # 没找到对应颜色
            if x2 == -1:
                return

            visited = [False] * N
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    tc = targetGrid[i][j]
                    if tc != c and not visited[tc]:
                        visited[tc] = True
                        inds[tc] += 1
                        g[c].append(tc)
            # print(g)

        N, m, n = 61, len(targetGrid), len(targetGrid[0])
        g, inds = [[] for _ in range(N)], [0] * N

        for i in range(0, N):
            build(i, inds)

        tot, q = 0, deque([i for i in range(N) if inds[i] == 0])
        while q:
            c = q.popleft()
            tot += 1

            for nc in g[c]:
                inds[nc] -= 1
                if inds[nc] == 0:
                    print(nc)
                    q.append(nc)

        return tot == N


if __name__ == '__main__':
    targetGrid = [[1, 1, 1, 1], [1, 1, 3, 3], [1, 1, 3, 4], [5, 5, 1, 4]]
    print(targetGrid)
    print(Solution().isPrintable(targetGrid))
