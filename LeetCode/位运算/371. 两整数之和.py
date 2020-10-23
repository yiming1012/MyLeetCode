"""
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        思路：加法运算=异或+左移
        1. 特别注意负数，如果是有符号的整数，范围为[-2^31,2^31-1],那么二进制的最高位就是符号位
        2. 将二进制的长度控制在32位
        @param a:
        @param b:
        @return:
        """
        mask = 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)


if __name__ == '__main__':
    a, b = -1, 2
    print(Solution().getSum(a, b))
