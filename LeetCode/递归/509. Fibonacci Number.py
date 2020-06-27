'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def fib1(self, N: int) -> int:
        '''
        执行用时 :1524 ms, 在所有 Python3 提交中击败了5.03%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.83%的用户
        思路：递归
        1. 注意递归的出口
        2. 递归的形式
        :param N:
        :return:
        '''
        if N <= 1:
            return N
        return self.fib1(N - 1) + self.fib1(N - 2)

    def fib2(self, N: int) -> int:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了46.70%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.83%的用户
        思路：斐波那契数列 F(N) = F(N - 1) + F(N - 2), for N > 1.
        1. 用两个变量a,b来保存前两位的值
        2. 迭代
        :param N:
        :return:
        '''
        if N <= 1:
            return N
        a, b = 0, 1
        while N > 1:
            a, b = b, a + b
            N -= 1
        return b

    def fib3(self, N: int) -> int:
        '''
        执行用时 :56 ms, 在所有 Python3 提交中击败了33.73%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.83%的用户
        思路：动态规划法
        1. 利用一个dp栈来记录前面两位的和
        :param N:
        :return:
        '''

        if N <= 1:
            return N
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    def fib4(self, N: int) -> int:
        """
        思路：记忆化递归
        """
        if N in cache:
            return cache[N]
        if N <= 1:
            return N
        cache[N] = self.fib4(N - 1) + self.fib4(N - 2)
        return cache[N]


if __name__ == '__main__':
    N = 6
    cache = {}
    print(Solution().fib1(N))
    print(Solution().fib2(N))
    print(Solution().fib3(N))
    print(Solution().fib4(N))
