"""
给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。

连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。

请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。



示例 1：

输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20
解释：

我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。
示例 2：

输入：points = [[3,12],[-2,5],[-4,1]]
输出：18
示例 3：

输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4
示例 4：

输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000
示例 5：

输入：points = [[0,0]]
输出：0


提示：

1 <= points.length <= 1000
-106 <= xi, yi <= 106
所有点 (xi, yi) 两两不同。
"""
import collections
from typing import List


class Solution:
    def minCostConnectPoints1(self, p: List[List[int]]) -> int:
        """
        思路：克鲁斯卡尔(Kruskal)
        @param p:
        @return:
        """
        n = len(p)
        edge = 0
        parent = [i for i in range(n)]

        def find(root):
            if root != parent[root]:
                parent[root] = find(parent[root])
            return parent[root]

        res = 0
        stack = []
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1])
                stack.append((d, i, j))

        stack.sort()
        for d, i, j in stack:
            i = find(i)
            j = find(j)
            if i != j:
                res += d
                parent[j] = i
                edge += 1
            if edge == n - 1:
                return res
        return res

    def minCostConnectPoints2(self, p: List[List[int]]) -> int:
        """
        思路：普里姆算法（Prim）
        @param p:
        @return:
        """
        n = len(p)
        dic = collections.defaultdict()
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1])
                dic[(i, j)] = d
                dic[(j, i)] = d

        dist = [float('inf')] * n
        dist[0] = 0
        visited = set()
        res = 0
        for i in range(n):
            node = -1
            mindist = float('inf')
            for j in range(n):
                if j not in visited and dist[j] < mindist:
                    node = j
                    mindist = dist[j]
            if node == -1:
                return res
            visited.add(node)
            res += dist[node]
            for j in range(n):
                if j not in visited and dic[(node, j)] < dist[j]:
                    dist[j] = dic[(node, j)]
        return res


if __name__ == '__main__':
    points = [[3, 12], [-2, 5], [-4, 1]]
    print(Solution().minCostConnectPoints1(points))
    print(Solution().minCostConnectPoints2(points))
