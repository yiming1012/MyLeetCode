"""
LCP 07. 传递信息
小朋友 A 在和 ta 的小伙伴们玩传信息游戏，游戏规则如下：

有 n 名玩家，所有玩家编号分别为 0 ～ n-1，其中小朋友 A 的编号为 0
每个玩家都有固定的若干个可传信息的其他玩家（也可能没有）。传信息的关系是单向的（比如 A 可以向 B 传信息，但 B 不能向 A 传信息）。
每轮信息必须需要传递给另一个人，且信息可重复经过同一个人
给定总玩家数 n，以及按 [玩家编号,对应可传递玩家编号] 关系组成的二维数组 relation。返回信息从小 A (编号 0 ) 经过 k 轮传递到编号为 n-1 的小伙伴处的方案数；若不能到达，返回 0。

示例 1：

输入：n = 5, relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], k = 3

输出：3

解释：信息从小 A 编号 0 处开始，经 3 轮传递，到达编号 4。共有 3 种方案，分别是 0->2->0->4， 0->2->1->4， 0->2->3->4。

示例 2：

输入：n = 3, relation = [[0,2],[2,1]], k = 2

输出：0

解释：信息不能从小 A 处经过 2 轮传递到编号 2

限制：

2 <= n <= 10
1 <= k <= 5
1 <= relation.length <= 90, 且 relation[i].length == 2
0 <= relation[i][0],relation[i][1] < n 且 relation[i][0] != relation[i][1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chuan-di-xin-xi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from functools import lru_cache
from typing import List


class Solution:
    def numWays1(self, n: int, relation: List[List[int]], k: int) -> int:
        """
        思路：动态规划法
        1. 类似Bellman Ford算法，遍历k次，每次更新每个节点的状态
        @param n:
        @param relation:
        @param k:
        @return:
        """
        dp = [[0] * n for _ in range(k + 1)]
        dp[0][0] = 1
        for i in range(1, k + 1):
            for u, v in relation:
                dp[i][v] += dp[i - 1][u]
        return dp[-1][-1]

    def numWays2(self, n: int, relation: List[List[int]], k: int) -> int:
        """
        思路：记忆化递归
        @param n:
        @param relation:
        @param k:
        @return:
        """
        graph = collections.defaultdict(list)
        for u, v in relation:
            graph[u].append(v)

        @lru_cache(None)
        def dfs(i, k):
            if i == n - 1 and k == 0:
                return 1
            if k == 0: return 0
            ans = 0
            for nex in graph[i]:
                ans += dfs(nex, k - 1)
            return ans

        res = dfs(0, k)
        dfs.cache_clear()
        return res


if __name__ == '__main__':
    n = 5
    relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
    k = 3
    print(Solution().numWays1(n, relation, k))
    print(Solution().numWays2(n, relation, k))