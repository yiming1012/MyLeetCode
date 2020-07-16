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
        1.每次找到最短的边，再由这条最短边扩散，知道确定所有的边都为最短的边
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

    """
        实现具体步骤：
        1.新建 dist 字典，存放网络节点n及对应的距离，并且初始化网络节点K的距离为0，其他节点距离为无穷大；
        2.新建 res 空字典，存放网络节点n及对应最短路径的距离；
        3.遍历 dist 字典，找出字典中最小的路径 min_dis 以及该路径对应的网络节点 ind，更新该网络节点 ind 所有相邻节点的距离（并且此相邻节点不在 res 字典中，即此相邻节点之前还未得出最短路径）；
        4.完成3步骤后，表示节点 ind 的最短路径为 min_dis，并且与之相邻节点也完成了距离的更新，此时节点 ind 已经不需要在下面的工作中进行遍历，所以删除 dist 字典中的 ind 节点，并将节点 ind 和它的最短路径 min_dis 插入到 res 中;
        5.循环3-4步骤直到 dist 所有节点遍历完或者 min_dis 为无穷大（即还有节点没有遍历到，此时函数返回-1）；
        6.返回 res 最大的最短路径，即为所有节点收到信号的时间
    """

    def networkDelayTime4(self, times: List[List[int]], N: int, K: int) -> int:
        dist = {i: float('inf') for i in range(1, N + 1)}
        dist[K] = 0
        res = {}
        while dist:
            min_dis = min(dist.values())
            print(min_dis)
            if min_dis == float('inf'):
                return -1
            for key, v in dist.items():
                if v == min_dis:
                    ind = key
            for time in times:
                if time[0] == ind and time[1] not in res.keys():
                    dist[time[1]] = min(dist[time[1]], dist[time[0]] + time[2])
            print(dist)
            res[ind] = min_dis
            dist.pop(ind)
        return max(res.values())


if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 3], [3, 4, 1], [2, 4, 3], [1, 4, 4]]
    N = 4
    K = 2
    # print(Solution().networkDelayTime1(times, N, K))
    # print(Solution().networkDelayTime2(times, N, K))
    # print(Solution().networkDelayTime3(times, N, K))
    print(Solution().networkDelayTime4(times, N, K))
