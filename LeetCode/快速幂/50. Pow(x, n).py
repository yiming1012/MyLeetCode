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
    def myPow1(self, x: float, n: int) -> float:
        """
        思路：迭代
        时间复杂度：O(N)
        """
        if n == 0:
            return 1
        if x == 0:
            if n > 0:
                return 0
            else:
                return inf
        res = 1
        flag = 1
        if n < 0:
            flag = -1
            n = abs(n)

        for i in range(n):
            res *= x

        return res if flag == 1 else 1 / res

    def myPow2(self, x: float, n: int) -> float:
        '''
        执行用时 :28 ms, 在所有 Python3 提交中击败了94.37%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.05%的用户
        思路：快速幂
        1、首先，任何数的0次幂都是
        2、负数的n次幂，为这个数绝对值的n次幂的倒数
        3、将n转化为2进制，如10对应的二进制为：1010，即n=1*(2**3）+0*(2**2)+1*(2**1)+0*(2**0)
        4、x**n中，x的（2**3）次幂等于x的（2**2）的平方
        时间复杂度：O(logN)
        :param x:
        :param n:
        :return:
        '''
        if n == 0:
            return 1
        if x == 0:
            if n > 0:
                return 0
            else:
                return inf
        res = 1
        flag = 1
        if n < 0:
            flag = -1
            n = abs(n)

        while n:
            # 如果最低位对应的是1，则累乘
            if n & 1:
                res *= x
            # 转换到下一位
            x *= x
            # 二进制右移
            n >>= 1

        return res if flag == 1 else 1 / res


if __name__ == '__main__':
    x, n = 2, 10
    print(Solution().myPow1(x, n))
    print(Solution().myPow2(x, n))
