"""
1780. 剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def cuttingRope1(self, n: int) -> int:
        mod = 10 ** 9 + 7
        res = 1
        if n <= 3:
            return n - 1

        while n > 4:
            res = res * 3 % mod
            n -= 3

        if n:
            res = res * n % mod
        return res

    def cuttingRope2(self, n: int) -> int:
        # 长度为n，索引从0到n而不是n-1
        # dp[i][j]:i到j的乘积
        dp = [[1] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            dp[i][i + 1] = 1
        for span in range(2, n + 1):
            for i in range(n - span + 1):
                j = i + span
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] * (j - k), (k - i) * dp[k][j], (k - i) * (j - k))
        return dp[0][-1]


if __name__ == '__main__':
    n = 10
    print(Solution().cuttingRope1(n))
    print(Solution().cuttingRope2(n))
