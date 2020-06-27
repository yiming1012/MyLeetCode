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
        """
        思路：类似链表相加
        1、从一端开始遍历，如果某一个长度不够，自动补零
        2、如果最后一位遍历完，还有进位，在最前面补1
        3、每次相加时，记录进位
        """
        m, n = len(a) - 1, len(b) - 1
        carry = 0
        s = ""
        while m >= 0 or n >= 0:
            carry += int(b[n]) if n >= 0 else 0
            carry += int(a[m]) if m >= 0 else 0
            s = str(carry & 1) + s
            carry >>= 1
            m -= 1
            n -= 1
        if carry:
            s = str(carry) + s
        return s

    def addBinary3(self, a, b):
        """
        思路：二进制求解
        """
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


if __name__ == '__main__':
    a = "111010"
    b = "1101"
    s = Solution()
    print(s.addBinary(a, b))
    print(s.addBinary3(a, b))
    print(s.addBinary4(a, b))
