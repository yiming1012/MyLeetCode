"""
有一根长度为 n 个单位的木棍，棍上从 0 到 n 标记了若干位置。例如，长度为 6 的棍子可以标记如下：



给你一个整数数组 cuts ，其中 cuts[i] 表示你需要将棍子切开的位置。

你可以按顺序完成切割，也可以根据需要更改切割的顺序。

每次切割的成本都是当前要切割的棍子的长度，切棍子的总成本是历次切割成本的总和。对棍子进行切割将会把一根木棍分成两根较小的木棍（这两根木棍的长度和就是切割前木棍的长度）。请参阅第一个示例以获得更直观的解释。

返回切棍子的 最小总成本 。

 

示例 1：



输入：n = 7, cuts = [1,3,4,5]
输出：16
解释：按 [1, 3, 4, 5] 的顺序切割的情况如下所示：

第一次切割长度为 7 的棍子，成本为 7 。第二次切割长度为 6 的棍子（即第一次切割得到的第二根棍子），第三次切割为长度 4 的棍子，最后切割长度为 3 的棍子。总成本为 7 + 6 + 4 + 3 = 20 。
而将切割顺序重新排列为 [3, 5, 1, 4] 后，总成本 = 16（如示例图中 7 + 4 + 3 + 2 = 16）。
示例 2：

输入：n = 9, cuts = [5,6,1,4,2]
输出：22
解释：如果按给定的顺序切割，则总成本为 25 。总成本 <= 25 的切割顺序很多，例如，[4，6，5，2，1] 的总成本 = 22，是所有可能方案中成本最小的。
 

提示：

2 <= n <= 10^6
1 <= cuts.length <= min(n - 1, 100)
1 <= cuts[i] <= n - 1
cuts 数组中的所有整数都 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-cost-to-cut-a-stick
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
import functools
import math
from typing import List


class Solution:
    def minCost1(self, n: int, cuts: List[int]) -> int:
        """
        思路：递归
        @param n:
        @param cuts:
        @return:
        """
        cuts = [0] + cuts + [n]
        cuts.sort()

        @functools.lru_cache(None)
        def dp(l, r):
            if l >= r - 1:
                return 0
            ans = math.inf
            for k in range(l + 1, r):
                new_v = dp(l, k) + dp(k, r) + cuts[r] - cuts[l]
                ans = min(ans, new_v)
            return ans if ans != math.inf else 0

        return dp(0, len(cuts) - 1)

    def minCost2(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        dic = collections.defaultdict()

        # @lru_cache(None)
        def dp(l, r):
            if l >= r - 1:
                return 0
            if (l, r) in dic:
                return dic[(l, r)]
            ans = float('inf')
            for k in range(l + 1, r):
                ans = min(ans, dp(l, k) + dp(k, r) + cuts[r] - cuts[l])
            dic[(l, r)] = ans
            return ans

        return dp(0, len(cuts) - 1)

    def minCost3(self, n: int, cuts: List[int]) -> int:
        """
        思路：区间dp
        @param n:
        @param cuts:
        @return:
        """
        cuts.sort()
        cuts = [0] + cuts + [n]
        dp = [[0 for i in range(len(cuts))] for i in range(len(cuts))]
        for i in range(len(cuts) - 1, -1, -1):
            for j in range(i + 1, len(cuts)):
                if i + 1 < j:
                    dp[i][j] = float('inf')
                    for k in range(i + 1, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                    dp[i][j] += cuts[j] - cuts[i]

        return dp[0][len(cuts) - 1]


if __name__ == '__main__':
    n = 7
    cuts = [1, 3, 4, 5]
    print(Solution().minCost1(n, cuts))
    print(Solution().minCost2(n, cuts))
    print(Solution().minCost3(n, cuts))
