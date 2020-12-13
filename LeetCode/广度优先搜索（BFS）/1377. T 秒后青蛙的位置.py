"""
1377. T 秒后青蛙的位置
给你一棵由 n 个顶点组成的无向树，顶点编号从 1 到 n。青蛙从 顶点 1 开始起跳。规则如下：

在一秒内，青蛙从它所在的当前顶点跳到另一个 未访问 过的顶点（如果它们直接相连）。
青蛙无法跳回已经访问过的顶点。
如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。
如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。
无向树的边用数组 edges 描述，其中 edges[i] = [fromi, toi] 意味着存在一条直接连通 fromi 和 toi 两个顶点的边。

返回青蛙在 t 秒后位于目标顶点 target 上的概率。



示例 1：



输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
输出：0.16666666666666666
解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，第 1 秒 有 1/3 的概率跳到顶点 2 ，然后第 2 秒 有 1/2 的概率跳到顶点 4，因此青蛙在 2 秒后位于顶点 4 的概率是 1/3 * 1/2 = 1/6 = 0.16666666666666666 。
示例 2：



输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
输出：0.3333333333333333
解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，有 1/3 = 0.3333333333333333 的概率能够 1 秒 后跳到顶点 7 。
示例 3：

输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6
输出：0.16666666666666666


提示：

1 <= n <= 100
edges.length == n-1
edges[i].length == 2
1 <= edges[i][0], edges[i][1] <= n
1 <= t <= 50
1 <= target <= n
与准确值误差在 10^-5 之内的结果将被判定为正确。
"""
import collections
from typing import List


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()
        queue = collections.deque()
        queue.append((1, 1))

        while queue and t >= 0:
            for i in range(len(queue)):
                node, p = queue.popleft()
                visited.add(node)

                choice = [nex for nex in graph[node] if nex not in visited]
                # 如果node为target且node为叶子节点，返回
                if node == target and (not choice or t == 0):
                    return p

                size = len(choice)
                for nex in choice:
                    queue.append((nex, p / size))
            t -= 1
        return 0


if __name__ == '__main__':
    n = 7
    edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
    t = 2
    target = 4
    print(Solution().frogPosition(n, edges, t, target))
