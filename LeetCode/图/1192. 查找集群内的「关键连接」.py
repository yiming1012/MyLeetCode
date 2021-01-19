"""
1192. 查找集群内的「关键连接」
力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。

它们之间以「服务器到服务器」点对点的形式相互连接组成了一个内部集群，其中连接 connections 是无向的。

从形式上讲，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。

「关键连接」是在该集群中的重要连接，也就是说，假如我们将它移除，便会导致某些服务器无法访问其他服务器。

请你以任意顺序返回该集群内的所有 「关键连接」。



示例 1：



输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
输出：[[1,3]]
解释：[[3,1]] 也是正确的。


提示：

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
不存在重复的连接
"""
import collections
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # 生成邻接表
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # 集合，注意排序让小的节点在前面，避免重复
        connections = set(map(tuple, (map(sorted, connections))))
        # DFS 访问每个节点的深度，只有访问过的路径有深度，初始化为 -1
        rank = [-1] * n

        def dfs(node, parent, depth):
            # 如果已经访问过该边，则已经记录了 rank
            if rank[node] >= 0:
                return rank[node]
            # 记录当前的 rank，默认会回溯 +1
            rank[node] = depth
            # 最大可能为 n
            min_depth = n
            for v in graph[node]:
                # 跳过父节点
                if v == parent:
                    continue
                # 获得子节点的最小深度
                back_depth = dfs(v, node, depth + 1)
                # 子节点比当前深度小，显然是环
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, v))))
                # 当前节点的最小深度也要记录下来，以便把整个环去掉
                min_depth = min(min_depth, back_depth)
            # 返回给父节点
            return min_depth

        dfs(0, -1, 0)
        return list(connections)
