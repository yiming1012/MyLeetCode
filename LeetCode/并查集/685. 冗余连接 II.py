"""
在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。

输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。

返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

示例 1:

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的有向图如下:
  1
 / \
v   v
2-->3
示例 2:

输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
输出: [4,1]
解释: 给定的有向图如下:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
注意:

二维数组大小的在3到1000范围内。
二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/redundant-connection-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class UnionFind(object):

    def __init__(self, n):
        self.pre = list(range(n))

    def find(self, x):
        if x != self.pre[x]:
            self.pre[x] = self.find(self.pre[x])
        return self.pre[x]

    def union(self, x1, x2):
        root1 = self.find(x1)
        root2 = self.find(x2)
        if root1 != root2:
            self.pre[root2] = root1
            return False

        return True


class Solution(object):
    def findRedundantDirectedConnection1(self, edges):
        """
        思路：并查集
        1. 判断是否存在入度为2和环
         先判断有没有入度为 2 的点：
         1. 没有入度为 2 的点：则一定有首尾相接的圈（意思是箭头方向全是一致，全是顺时针或者逆时针），
         此时可以按照无向图的情形处理，删除最后出现的多余的边。
         2. 有入度为 2 的点 c，两条边先后出现的顺序是 [a,c] 和 [b,c]：在边集中去掉 [b,c]，即不加入到并查集中，
         判断剩下的边集中是否存在圈： a. 如果存在圈，则删掉 [a,c]。 b. 不存在圈，则删掉 [b,c].

        """
        n = len(edges)
        uf = UnionFind(n + 1)

        last = []
        parent = {}
        candidates = []
        for st, ed in edges:
            if ed in parent:
                candidates.append([parent[ed], ed])
                candidates.append([st, ed])
                # print(candidates)
            else:
                parent[ed] = st
                if uf.union(st, ed):
                    last = [st, ed]
                    # print(last)

        if not candidates:
            return last
        # print(candidates)
        return candidates[0] if last else candidates[1]

    def findRedundantDirectedConnection2(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = {i: i for i in range(n + 1)}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        root = {}
        ind = []
        ring = None
        for u, v in edges:
            if v in root:
                ind.append([root[v], v])
                ind.append([u, v])
            else:
                root[v] = u
                a, b = find(u), find(v)
                if a != b:
                    parent[b] = a
                else:
                    ring = [u, v]
        # 如果没有入度为2的，去掉构成环的边
        if not ind:
            return ring
        # 如果还有环，说明需要删掉前面的一条，因为后面的一条边没加到ind中
        return ind[0] if ring else ind[1]


if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [3, 1], [4, 1]]
    # edges = [[1, 2], [2, 3], [4, 1], [5, 4], [4, 3]]
    print(Solution().findRedundantDirectedConnection1(edges))
