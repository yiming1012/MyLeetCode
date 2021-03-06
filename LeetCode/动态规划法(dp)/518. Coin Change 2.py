'''
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from functools import lru_cache
from typing import List


class Solution:
    def change1(self, amount: int, coins: List[int]) -> int:
        '''
        执行用时 :220 ms, 在所有 Python3 提交中击败了53.19%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了57.14%的用户
        :param amount:
        :param coins:
        :return:
        '''
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
            print(dp)
        return dp[-1]

    def change2(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dfs(r, i):
            if r == 0:
                return 1
            if r < 0 or i == len(coins):
                return 0
            return dfs(r - coins[i], i) + dfs(r, i + 1)

        return dfs(amount, 0)


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    s = Solution()
    print(s.change1(amount, coins))
    print(s.change2(amount, coins))
