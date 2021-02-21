"""
131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        dp = [[False] * n for _ in range(n)]
        for span in range(1, n + 1):
            for i in range(n - span + 1):
                j = i + span - 1
                if span == 1:
                    dp[i][j] = True
                elif span == 2:
                    dp[i][j] = True if s[i] == s[j] else False
                else:
                    dp[i][j] = dp[i + 1][j - 1] if s[i] == s[j] else False

        def dfs(cur, arr):
            if cur == n:
                res.append(arr.copy())
                return
            for i in range(cur, n):
                if dp[cur][i]:
                    dfs(i + 1, arr + [s[cur:i + 1]])

        dfs(0, [])
        return res


if __name__ == '__main__':
    s = "aab"
    print(Solution().partition(s))
