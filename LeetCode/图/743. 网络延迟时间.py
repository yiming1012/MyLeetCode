"""
有 N 个网络节点，标记为 1 到 N。

给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。

现在，我们从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。

 

示例：



输入：times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
输出：2
 

注意:

N 的范围在 [1, 100] 之间。
K 的范围在 [1, N] 之间。
times 的长度在 [1, 6000] 之间。
所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 0 <= w <= 100。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/network-delay-time
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def networkDelayTime1(self, times: List[List[int]], N: int, K: int) -> int:
        """
        思路：迪杰斯特拉算法
        1.每次找到最短的边，再由这条最短边松弛其他相邻的边，直到确定所有的边都为最短的边
        """
        graph = collections.defaultdict(list)
        for time in times:
            a, b, c = time
            graph[a].append((b, c))

        dist = {node: float('inf') for node in range(1, N + 1)}
        dist[K] = 0
        visited = [False] * (N + 1)
        while True:
            index = -1
            dis = float('inf')
            for i in range(1, N + 1):
                if not visited[i] and dist[i] < dis:
                    dis = dist[i]
                    index = i
            if index == -1:
                break
            visited[index] = True
            for v, w in graph[index]:
                dist[v] = min(dist[v], dist[index] + w)
        res = max(dist.values())
        return res if res != float('inf') else -1

    def networkDelayTime2(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in range(1, N + 1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1

    def networkDelayTime3(self, times, N, K):
        """
        思路：迪杰斯特拉算法
        1.每次找到最短的边，再由这条最短边松弛其他相邻的边，直到确定所有的边都为最短的边
        """
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N + 1)}
        seen = [False] * (N + 1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N + 1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1

    def networkDelayTime5(self, times: List[List[int]], N: int, K: int) -> int:
        """
        思路：迪杰斯特拉算法+堆优化
        1. 将节点v和当前K离v最近的距离d加入到小根堆里面heapq.heappush(pq,(d,v))，这样每次堆顶元素都是最小值
        2. 时间复杂度: Nlog(N)
        """
        import heapq
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        pq = [(0, K)]
        visited = [False for _ in range(N + 1)]
        dist = {node: float('inf') for node in range(1, N + 1)}
        dist[K] = 0
        while pq:
            d, node = heapq.heappop(pq)
            if d == float('inf'):
                return -1
            visited[node] = True
            for v, w in graph[node]:
                if not visited[v] and dist[v] > dist[node] + w:
                    dist[v] = dist[node] + w
                    heapq.heappush(pq, (dist[v], v))
        res = max(dist.values())
        return -1 if res == float('inf') else res

    def networkDelayTime6(self, times: List[List[int]], N: int, K: int) -> int:
        """
        思路：Floyd(多源最短路径)
        1. 解决任意两点间的最短距离
        2. 时间复杂度: N**3
        """
        graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
        for u, v, w in times:
            graph[u][v] = w
        graph[K][K] = 0
        for k in range(1, N + 1):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        res = max(graph[K][1:])
        return -1 if res == float('inf') else res


if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 3], [3, 4, 1], [2, 4, 3], [1, 4, 4], [4, 2, 1], [4, 3, 2]]
    N = 4
    K = 1
    print(Solution().networkDelayTime1(times, N, K))
    print(Solution().networkDelayTime2(times, N, K))
    print(Solution().networkDelayTime3(times, N, K))
    print(Solution().networkDelayTime5(times, N, K))
    print(Solution().networkDelayTime6(times, N, K))
