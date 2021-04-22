"""
265. 粉刷房子 II
假如有一排房子，共 n 个，每个房子可以被粉刷成 k 种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x k 的矩阵来表示的。

例如，costs[0][0] 表示第 0 号房子粉刷成 0 号颜色的成本花费；costs[1][2] 表示第 1 号房子粉刷成 2 号颜色的成本花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。

注意：

所有花费均为正整数。

示例：

输入: [[1,5,3],[2,9,4]]
输出: 5
解释: 将 0 号房子粉刷成 0 号颜色，1 号房子粉刷成 2 号颜色。最少花费: 1 + 4 = 5;
     或者将 0 号房子粉刷成 2 号颜色，1 号房子粉刷成 0 号颜色。最少花费: 3 + 2 = 5.
进阶：
您能否在 O(nk) 的时间复杂度下解决此问题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paint-house-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


class Solution:
    def minCostII1(self, costs: List[List[int]]) -> int:
        """
        思路：需要相邻两个颜色不同，遍历两个颜色不同的情况
        @param costs:
        @return:
        """
        if not costs: return 0
        N, K = len(costs), len(costs[0])
        if N == 1: return min(costs[0])
        if K == 1: return min([c[0] for c in costs])
        dp = [[float('inf')] * K for _ in range(N + 1)]
        dp[0] = [0] * K
        for i in range(1, N + 1):
            for j in range(K):
                for k in range(K):
                    if j != k:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i - 1][j])
        return min(dp[-1])

    def minCostII2(self, costs) -> int:
        def min2(lst):
            """
            return the min elements of lst, except res[min_v_index] = min2
            """
            print(lst)
            if len(lst) == 1:
                return lst
            m1, m2, i1, i2 = float('inf'), float('inf'), 0, 0
            for j, v in enumerate(lst):
                if v < m1:
                    m2, i2 = m1, i1
                    m1, i1 = v, j
                elif v < m2:
                    m2, i2 = v, j
            res = [m1] * n
            res[i1] = m2
            return res

        m = len(costs)
        if m == 0:
            return 0
        n = len(costs[0])
        dp = min2(costs[0])
        for i in range(1, m):
            dp = min2([costs[i][j] + dp[j] for j in range(n)])
        # update costs based on costs, all costs value add min(dp) except the one got the same index with min(dp)
        return min(dp)


if __name__ == '__main__':
    costs = [[1, 5, 3], [2, 9, 4]]
    print(Solution().minCostII1(costs))
    print(Solution().minCostII2(costs))
