'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

'''
import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        执行用时 :1408 ms, 在所有 Python3 提交中击败了81.06%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了20.77%的用户
        :param coins:
        :param amount:
        :return:
        '''
        if len(coins) == 0 or amount < 0:
            return -1

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                # print(coin, i)
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        '''
        执行用时 :1408 ms, 在所有 Python3 提交中击败了81.06%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了20.77%的用户
        :param coins:
        :param amount:
        :return:
        '''
        if len(coins) == 0 or amount < 0:
            return -1

        # 逆序排列
        coins.sort(reverse=True)
        #
        ans = sys.maxsize
        ans = self.dfs(coins, 0, amount, 0, ans)
        # dfs:depth-first-search
        return ans if ans != sys.maxsize else -1

    def dfs(self, coins, index, amount, count, ans):
        coin = coins[index]
        if index == len(coins) - 1:
            if amount % coin == 0:
                ans = min(ans, count + amount // coin)
        else:
            for i in range(amount // coin, -1, -1):
                if i + count >= ans:
                    break
                self.dfs(coins, index + 1, amount - i * coin, i + count, ans)

        return ans


if __name__ == '__main__':
    coins = [1, 2, 5]
    coins2 = [3]
    amount = 11
    s = Solution()
    print(s.coinChange2(coins, amount))
