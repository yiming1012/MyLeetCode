"""
给定一个正整数 n，你可以做如下操作：

1. 如果 n 是偶数，则用 n / 2替换 n。
2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
n 变为 1 所需的最小替换次数是多少？

示例 1:

输入:
8

输出:
3

解释:
8 -> 4 -> 2 -> 1
示例 2:

输入:
7

输出:
4

解释:
7 -> 8 -> 4 -> 2 -> 1
或
7 -> 6 -> 3 -> 2 -> 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-replacement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import lru_cache


class Solution:
    def integerReplacement1(self, n: int) -> int:
        """
        思路：记忆化递归-标准库
        @param n:
        @return:
        """

        @lru_cache(None)
        def dfs(n):
            if n == 1:
                return 0

            ans = 0
            if n & 1:
                ans += 1 + min(dfs(n + 1), dfs(n - 1))
            else:
                ans += 1 + dfs(n // 2)
            return ans

        return dfs(n)

    def integerReplacement2(self, n: int) -> int:
        """
        思路：记忆化递归-备忘录
        @param n:
        @return:
        """

        def dfs(n):
            if n in memo:
                return memo[n]

            ans = 0
            if n & 1:
                ans += 1 + min(dfs(n + 1), dfs(n - 1))
            else:
                ans += 1 + dfs(n // 2)
            memo[n] = ans
            return ans

        memo = {1: 0}
        return dfs(n)
