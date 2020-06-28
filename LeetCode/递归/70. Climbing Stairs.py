'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        执行用时 :56 ms, 在所有 Python3 提交中击败了8.78%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.58%的用户
        思路：f(n)=f(n-1)+f(n-2),所以只需要保存最近的两个数即可
        :param n:
        :return:
        '''
        if n <= 2:
            return n
        a, b = 1, 2
        while n > 2:
            a, b = b, a + b
            n -= 1
        return b

    def climbStairs(self, n: int) -> int:
        '''
        思路：递归超时
        :param n:
        :return:
        '''

        def helper(n):
            if n <= 2:
                return n
            return helper(n - 1) + helper(n - 2)

        return helper(n)

    def climbStairs(self, n: int) -> int:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了61.21%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.58%的用户
        思路：动态规划法
        :param n:
        :return:
        '''
        if n <= 2:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
