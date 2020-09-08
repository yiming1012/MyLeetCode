"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        执行用时 :3096 ms, 在所有 Python3 提交中击败了12.09%的用户
        内存消耗 :39 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：
        1、求最长回文子序列的长度，可以看做s和s[::-1]的最长子序列
        """
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                if s[i] == s[n - j - 1]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[-1][-1]

    def longestPalindromeSubseq2(self, s: str) -> int:
        """
        执行用时 :1416 ms, 在所有 Python3 提交中击败了84.56%的用户
        内存消耗 :30.3 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：动态规划法
        1、建立一个二维的dp数组，dp[i][j]表示从i到j最长的回文长度
        2、当s[i]==s[j]时，dp[i][j]=dp[i+1][j-1]+2
        3、当s[i]!=s[j]时，dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]
