'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from math import inf


class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        执行用时 :28 ms, 在所有 Python3 提交中击败了94.37%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.05%的用户
        思路：快速幂
        :param x:
        :param n:
        :return:
        '''
        if x == 0:
            if n < 0:
                return inf
            elif n == 0:
                return 1
            else:
                return 0

        i = abs(n)
        r = 1.0
        while i != 0:
            if i % 2 != 0:
                r *= x
            x *= x
            i //= 2
        return r if n > 0 else 1 / r
