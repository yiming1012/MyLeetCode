"""
1269. 停在原地的方案数
有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。

每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。

给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。

由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。

 

示例 1：

输入：steps = 3, arrLen = 2
输出：4
解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动
示例  2：

输入：steps = 2, arrLen = 4
输出：2
解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
向右，向左
不动，不动
示例 3：

输入：steps = 4, arrLen = 2
输出：8
 

提示：

1 <= steps <= 500
1 <= arrLen <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import lru_cache


class Solution:
    def numWays1(self, s: int, a: int) -> int:
        """
        思路：记忆化递归
        @param s:
        @param a:
        @return:
        """
        mod = 10 ** 9 + 7
        memo = {}

        def dfs(index, s):
            if index == 0 and s == 0:
                return 1
            if s < 0:
                return 0
            if (index, s) in memo:
                return memo[(index, s)]

            ans = 0
            # 不走
            ans += dfs(index, s - 1)
            # 向右走
            if index < a - 1:
                ans += dfs(index + 1, s - 1)
            # 向左走
            if index > 0:
                ans += dfs(index - 1, s - 1)
            memo[(index, s)] = ans
            return ans

        return dfs(0, s) % mod

    def numWays2(self, s: int, a: int) -> int:
        """
        思路：动态规划法
        1. 超时
        @param s:
        @param a:
        @return:
        """
        mod = 10 ** 9 + 7
        dp = [[0] * (a + 1) for _ in range(s + 1)]
        dp[0][0] = 1
        for i in range(1, s + 1):
            for j in range(a):
                for k in [-1, 0, 1]:
                    if 0 <= j - k < a:
                        dp[i][j] += dp[i - 1][j - k]

        return dp[-1][0] % mod

    def numWays3(self, steps: int, arrLen: int) -> int:
        """
        写法优雅、美观
        @param steps:
        @param arrLen:
        @return:
        """
        @lru_cache(None)
        def dfs(cur, s):
            if cur == -1 or cur == arrLen or cur > s:
                return 0
            if cur == 0 and s == 0:
                return 1

            return dfs(cur, s - 1) + dfs(cur - 1, s - 1) + dfs(cur + 1, s - 1)

        mod = 10 ** 9 + 7
        ans = dfs(0, steps)
        dfs.cache_clear()
        return ans % mod


if __name__ == '__main__':
    steps = 3
    arrLen = 2
    print(Solution().numWays1(steps, arrLen))
    print(Solution().numWays2(steps, arrLen))
    print(Solution().numWays3(steps, arrLen))
