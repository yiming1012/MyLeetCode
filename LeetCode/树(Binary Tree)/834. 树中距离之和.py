"""
给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。

第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。

返回一个表示节点 i 与其他所有节点距离之和的列表 ans。

示例 1:

输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
输出: [8,12,6,10,10,10]
解释:
如下为给定的树的示意图：
  0
 / \
1   2
   /|\
  3 4 5

我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
说明: 1 <= N <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-distances-in-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        """
        思路：dfs
        @param N:
        @param edges:
        @return:
        """
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        ans = [0] * N
        cnt = [1] * N

        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    cnt[node] += cnt[child]
                    ans[node] += ans[child] + cnt[child]

        dfs()

        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] + N - 2 * cnt[child]
                    dfs2(child, node)

        dfs2()
        return ans


if __name__ == '__main__':
    N = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(Solution().sumOfDistancesInTree(N, edges))
