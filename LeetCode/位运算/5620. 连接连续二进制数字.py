"""
5620. 连接连续二进制数字
给你一个整数 n ，请你将 1 到 n 的二进制表示连接起来，并返回连接结果对应的 十进制 数字对 109 + 7 取余的结果。



示例 1：

输入：n = 1
输出：1
解释：二进制的 "1" 对应着十进制的 1 。
示例 2：

输入：n = 3
输出：27
解释：二进制下，1，2 和 3 分别对应 "1" ，"10" 和 "11" 。
将它们依次连接，我们得到 "11011" ，对应着十进制的 27 。
示例 3：

输入：n = 12
输出：505379714
解释：连接结果为 "1101110010111011110001001101010111100" 。
对应的十进制数字为 118505380540 。
对 109 + 7 取余后，结果为 505379714 。


提示：

1 <= n <= 105
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        思路：注意在运行过程中也要取模，不然会超时
        @param n:
        @return:
        """
        mod = 10 ** 9 + 7
        res = 0
        size = 0

        for i in range(1, n + 1):
            # 递推求二进制位数
            if i & (i - 1) == 0:
                size += 1
            res <<= size
            res += i
            res %= mod
        return res % mod


if __name__ == '__main__':
    n = 3
    print(Solution().concatenatedBinary(n))
