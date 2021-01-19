"""
1129. 颜色交替的最短路径
在一个有向图中，节点分别标记为 0, 1, ..., n-1。这个图中的每条边不是红色就是蓝色，且存在自环或平行边。

red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的蓝色有向边。

返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。

 

示例 1：

输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
输出：[0,1,-1]
示例 2：

输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
输出：[0,1,-1]
示例 3：

输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
输出：[0,-1,-1]
示例 4：

输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
输出：[0,1,2]
示例 5：

输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
输出：[0,1,1]
 

提示：

1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-path-with-alternating-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # 0代表红色 1代表蓝色
        graph = {
            0: collections.defaultdict(list),
            1: collections.defaultdict(list)
        }

        for i, j in red_edges:
            graph[0][i].append(j)
        for i, j in blue_edges:
            graph[1][i].append(j)

        # 以i结尾的红蓝长度
        path = [[float('inf')] * 2 for _ in range(n)]
        path[0][0], path[0][1] = 0, 0
        # (本点前一条线的颜色, 本点坐标, 路径长度), 初始化队列, 原点既可以从红开始也可以从蓝开始
        queue = collections.deque([(0, 0, 0), (1, 0, 0)])
        while queue:
            color, start, step = queue.popleft()
            color ^= 1
            for nex in graph[color][start]:
                if step + 1 < path[nex][color]:
                    path[nex][color] = step + 1
                    queue.append((color, nex, step + 1))
        # 获取以i结尾的最短的红蓝交替路径
        ans = [-1] * n
        for i in range(n):
            min_ = min(path[i])
            if min_ != float('inf'):
                ans[i] = min_
        return ans


if __name__ == '__main__':
    n = 3
    red_edges = [[0, 1], [1, 2]]
    blue_edges = []
    print(Solution().shortestAlternatingPaths(n, red_edges, blue_edges))
