"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def integerBreak1(self, n: int) -> int:
        """
        思路：动态规划法
        1. i:当前n的大小；
        2. j:最后一段划分的长度
        3. 当划分了最后一段后，前面的有两种情况：
            1）i-j:表示没有分段
            2）dp[i-j]:表示有分段
        """
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], max(i - j, dp[i - j]) * j)
        return dp[-1]

    def integerBreak2(self, n: int) -> int:
        """
        思路：dfs超时
        """
        res = 1

        def dfs(remain, count, presum):
            nonlocal res
            if remain == 0:
                if count > 1:
                    res = max(res, presum)
                return

            for i in range(1, remain + 1):
                dfs(remain - i, count + 1, presum * i)

        dfs(n, 0, 1)
        return res

    def integerBreak3(self, n: int) -> int:
        """
        思路：dfs+记忆化（memo）
        """
        res = 1

        def dfs(remain, count, presum):
            nonlocal res
            if remain == 0:
                if count > 1:
                    res = max(res, presum)
                return

            for i in range(1, remain + 1):
                dfs(remain - i, count + 1, presum * i)

        dfs(n, 0, 1)
        return res

    def integerBreak3(self, n: int) -> int:
        """
        思路：记忆化递归 dfs+memo
        1. memo记录每个n对应的最大值，如果这个值已经计算过，就直接用这个值
        2. 每次递归后，记录n对应的最大值
        3. 递归返回值：memo[n]
        4. 递归出口：n==1 or demo[n]!=-
        """
        memo = [-1] * (n + 1)

        def dfs(n):
            if memo[n] != -1:
                return memo[n]
            if n == 1:
                return 1

            res = 1
            for i in range(1, n):
                res = max(res, i * (n - i), i * dfs(n - i))
            memo[n] = res
            return memo[n]

        return dfs(n)


if __name__ == '__main__':
    n = 30
    print(Solution().integerBreak1(n))
    # print(Solution().integerBreak2(n))
    print(Solution().integerBreak3(n))
