"""
518. 零钱兑换 II
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。



示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10]
输出: 1


注意:

你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数
"""
from typing import List


class Solution:
    def change1(self, amount: int, coins: List[int]) -> int:
        """
        1. 每个物品可以用无数次
        2. dp[i][j]表示用硬币的前i个可以凑成金额j的个数
        """
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
        return dp[-1][-1]

    def change2(self, amount: int, coins: List[int]) -> int:
        """
        1. 每个物品可以用无数次
        2. 每次会用到上面一层的结果，可以将上面dp[i-1][j]改为dp[j]
        """
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change1(amount, coins))
    print(Solution().change2(amount, coins))
