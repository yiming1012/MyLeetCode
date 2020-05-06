'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了19.33%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了24.78%的用户
        :param a:
        :param b:
        :return:
        '''
        s = ""
        flag = 0
        m, n = len(a), len(b)
        f = abs(m - n) * "0"
        if m > n:
            b = f + b
        else:
            a = f + a

        print(a, b)

        while m > 0 or n > 0 or flag == 1:
            res = (int(a[m - 1] if m > 0 else '0') + int(b[n - 1] if n > 0 else '0') + flag)
            flag = res // 2
            s = str(res % 2) + s
            m -= 1
            n -= 1
        return s

    def addBinary2(self, a: str, b: str) -> str:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了39.05%的用户
        内存消耗 :13.3 MB, 在所有 Python3 提交中击败了24.78%的用户
        :param self: 
        :param a: 
        :param b: 
        :return: 
        '''
        s = ""
        flag = 0
        m, n = len(a), len(b)

        if m > n:
            b = (m - n) * "0" + b
            n = m

        else:
            a = (n - m) * "0" + a
            m = n

        while m > 0:
            res = int(a[m - 1]) + int(b[m - 1]) + flag
            flag = res // 2
            s = str(res % 2) + s
            m -= 1

        if flag == 1:
            s = '1' + s
        return s

    def addBinary3(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary4(self, a: str, b: str) -> str:
        '''
        当不允许使用加法时，可采用位运算来求解
        :param a:
        :param b:
        :return:
        '''
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]


a = "111010"
b = "1101"

s = Solution()
print(s.addBinary3(a, b))
