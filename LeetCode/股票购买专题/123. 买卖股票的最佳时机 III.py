"""
123. 买卖股票的最佳时机III
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import lru_cache
from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        """
        思路：记忆化递归
        @param prices:
        @return:
        """
        if not prices:
            return 0

        n = len(prices)

        @lru_cache(None)
        def dfs(index, status, k):
            if index == n or k == 0:
                return 0

            a, b, c = 0, 0, 0
            a = dfs(index + 1, status, k)
            # status:0 买入 1 卖出
            if status:
                b = dfs(index + 1, 0, k - 1) + prices[index]
            else:
                c = dfs(index + 1, 1, k) - prices[index]
            return max(a, b, c)

        return dfs(0, 0, 2)

    def maxProfit2(self, prices: List[int]) -> int:
        """
        思路：动态规划法
        @param prices:
        @return:
        """
        if not prices:
            return 0

        n = len(prices)
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]
        for i in range(3):
            dp[0][i][0] = -prices[0]

        for i in range(1, n):
            for j in range(1, 3):
                # 买入
                dp[i][j - 1][0] = max(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1] - prices[i])
                # 卖出
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] + prices[i])

        return dp[-1][2][1]


if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(Solution().maxProfit1(prices))
    print(Solution().maxProfit2(prices))
