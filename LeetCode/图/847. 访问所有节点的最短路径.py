"""
给出 graph 为有 N 个节点（编号为 0, 1, 2, ..., N-1）的无向连通图。 

graph.length = N，且只有节点 i 和 j 连通时，j != i 在列表 graph[i] 中恰好出现一次。

返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。

 

示例 1：

输入：[[1,2,3],[0],[0],[0]]
输出：4
解释：一个可能的路径为 [1,0,2,0,3]
示例 2：

输入：[[1],[0,2,4],[1,3,4],[2],[1,2]]
输出：4
解释：一个可能的路径为 [0,1,4,2,3]
 

提示：

1 <= graph.length <= 12
0 <= graph[i].length < graph.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def shortestPathLength(self, graph):
        """
        思路：BFS
        1. 状态压缩利用state存储被访问过的节点
        2. 队列queue存储(state,node)
        3. dist存储走到当前node且包含state中k个节点的最短路径，dist[(state,node)]=d
        @param graph:
        @return:
        """
        n = len(graph)
        queue = collections.deque()
        dist = collections.defaultdict(lambda: float('inf'))
        for i in range(n):
            queue.append((1 << i, i))
            dist[(1 << i, i)] = 0

        while queue:
            state, node = queue.popleft()
            d = dist[(state, node)]
            if state == 2 ** n - 1:
                return d
            for k in graph[node]:
                new_state = state | (1 << k)
                if d + 1 < dist[(new_state, k)]:
                    dist[(new_state, k)] = d + 1
                    queue.append((new_state, k))
        return -1

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target = (1 << n) - 1  # 目标即全部已访问
        dp = [[float('inf')] * n for _ in range(target + 1)]  # dp[i][j]：走到j结点且已访问记录为i时的当前最小步数
        for i in range(n):
            dp[1 << i][i] = 0  # 初始化所有起点的dp为0
        q = [(1 << i, i) for i in range(n)]  # BFS状态队列：（已访问记录，当前位置）
        while q:
            visited, at = q.pop(0)
            if visited == target:  # 达到目标
                return dp[visited][at]
            step = dp[visited][at] + 1  # 下一步的步数
            for next in graph[at]:  # 访问邻居
                _visited = visited | (1 << next)  # 走出该步后的新访问记录
                if step < dp[_visited][next]:  # 如果比以前更快达到该状态
                    dp[_visited][next] = step  # 更新dp
                    q.append((_visited, next))  # 入队BFS
        return -1  # 不存在这样的路径


if __name__ == '__main__':
    graph = [[1, 2, 3], [0], [0], [0]]
    print(Solution().shortestPathLength(graph))
