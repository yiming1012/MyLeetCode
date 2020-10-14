"""
想象一下你是个城市基建规划者，地图上有 N 座城市，它们按以 1 到 N 的次序编号。

给你一些可连接的选项 conections，其中每个选项 conections[i] = [city1, city2, cost] 表示将城市 city1 和城市 city2 连接所要的成本。
（连接是双向的，也就是说城市 city1 和城市 city2 相连也同样意味着城市 city2 和城市 city1 相连）。

返回使得每对城市间都存在将它们连接在一起的连通路径（可能长度为 1 的）最小成本。该最小成本应该是所用全部连接代价的综合。
如果根据已知条件无法完成该项任务，则请你返回 -1。

示例 1：

输入：N = 3, conections = [[1,2,5],[1,3,6],[2,3,1]]
输出：6
解释：
选出任意 2 条边都可以连接所有城市，我们从中选取成本最小的 2 条。

示例 2：

输入：N = 4, conections = [[1,2,3],[3,4,4]]
输出：-1
解释：
即使连通所有的边，也无法连接所有城市。

提示：

1. 1 <= N <= 10000
2. 1 <= conections.length <= 10000
3. 1 <= conections[i][0], conections[i][1] <= N
4. 0 <= conections[i][2] <= 10^5
5. conections[i][0] != conections[i][1]
"""
from typing import List


class Solution:
    def minimumCost1(self, N: int, connections: List[List[int]]) -> int:
        """
        思路：kruskal（并查集）
        1. 将所有边按照权重大小排序
        2. 遍历排好序的边集合，通过并查集相连
            a. 如果当前边的两个顶点，已在最小生成树中，跳过
            b. 如果当前边的两个顶点，不在最小生成树中，则将该边加入到最小生成树中
        3. 如果构成的图的边等于顶点数-1，退出
        @param N:
        @param connections:
        @return:
        """
        if len(connections) < N - 1:
            return -1
        connections.sort(key=lambda a: a[2])
        parent = [i for i in range(N)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        res, e, k = 0, 0, 0
        while e < N - 1:
            u, v, w = connections[k]
            k += 1
            x, y = find(u - 1), find(v - 1)
            if x != y:
                e += 1
                res += w
                parent[x] = y
        return res

    def minimumCost2(self, N: int, connections: List[List[int]]) -> int:
        parent = [j for j in range(N)]
        connections.sort(key=lambda x: x[2])
        print(connections)
        edge = 0
        res = 0

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v, w in connections:
            x = find(u - 1)
            y = find(v - 1)
            if x != y:
                edge += 1
                parent[y] = x
                res += w
            if edge == N - 1:
                return res

        return res


if __name__ == '__main__':
    N = 3
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    print(Solution().minimumCost1(N, connections))
    print(Solution().minimumCost2(N, connections))
