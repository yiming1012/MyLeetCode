"""
261. 以图判树
给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。

示例 1：

输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
输出: true
示例 2:

输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
输出: false
注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表 edges 中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/graph-valid-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.part = n
        self.parent = [x for x in range(n)]
        self.size = [1 for _ in range(n)]

    def Find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        return self.Find(self.parent[x])

    def Union(self, x: int, y: int) -> bool:
        root_x = self.Find(x)
        root_y = self.Find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.part -= 1

    def connected(self, x: int, y: int) -> bool:
        return self.Find(x) == self.Find(y)

    def get_part_size(self, x: int) -> int:
        root_x = self.Find(x)
        return self.size[root_x]


class Solution:
    # 方法一：并查集
    def validTree1(self, n: int, edges: List[List[int]]) -> bool:
        UF = UnionFind(n)
        for x, y in edges:
            if not UF.Union(x, y):  # 失败了，说明已经在一个连通域中了。再连接就是环了
                return False
        return UF.part == 1

    # 方法二：DFS
    def validTree2(self, n: int, edges: List[List[int]]) -> bool:
        m = len(edges)
        if n != m + 1: return False
        graph = collections.defaultdict(set)
        visited = set()
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(root, fa=None):
            if root in visited:
                return False
            visited.add(root)
            for nex in graph[root]:
                if nex != fa:
                    dfs(nex, root)

        dfs(0)
        return len(visited) == n
