"""
1245. 树的直径
给你这棵「无向树」，请你测算并返回它的「直径」：这棵树上最长简单路径的 边数。

我们用一个由所有「边」组成的数组 edges 来表示一棵无向树，其中 edges[i] = [u, v] 表示节点 u 和 v 之间的双向边。

树上的节点都已经用 {0, 1, ..., edges.length} 中的数做了标记，每个节点上的标记都是独一无二的。



示例 1：



输入：edges = [[0,1],[0,2]]
输出：2
解释：
这棵树上最长的路径是 1 - 0 - 2，边数为 2。
示例 2：



输入：edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
输出：4
解释：
这棵树上最长的路径是 3 - 2 - 1 - 4 - 5，边数为 4。


提示：

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
edges 会形成一棵无向树
"""
import collections
from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        res = 0

        def dfs(root):
            nonlocal res
            pre = 0
            visited.add(root)
            for nex in graph[root]:
                if nex not in visited:
                    cur = dfs(nex)
                    res = max(res, cur + pre)
                    print(root, res)
                    if cur > pre:
                        pre = cur
            return pre + 1

        dfs(0)
        return res


if __name__ == '__main__':
    edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
    print(Solution().treeDiameter(edges))
