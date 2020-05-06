'''
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents. (The result may be large, so you should return it modulo 1000000007)

Example1:

 Input: n = 5
 Output: 2
 Explanation: There are two ways:
5=5
5=1+1+1+1+1
Example2:

 Input: n = 10
 Output: 4
 Explanation: There are four ways:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
Notes:

You can assume:

0 <= n <= 1000000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def waysToChange(self, n: int) -> int:
        '''
        执行用时 :1512 ms, 在所有 Python3 提交中击败了42.07%的用户
        内存消耗 :64.5 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：经典的背包问题
        :param n:
        :return:
        '''
        coins = [5, 10, 25]
        dp = [1] * (n + 1)

        for coin in coins:
            for i in range(coin, n + 1):
                dp[i] += dp[i - coin]

        return dp[-1] % 1000000007


if __name__ == '__main__':
    n = 20
    s = Solution()
    print(s.waysToChange(5))
    print(s.waysToChange(10))
    print(s.waysToChange(15))
    print(s.waysToChange(20))