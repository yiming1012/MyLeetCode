"""
计算所有公共子序列
给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。

（如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，那么 S 就是 T 的子序列）



示例：

输入：str1 = "abac", str2 = "cab"
输出："cabac"
解释：
str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。
str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
最终我们给出的答案是满足上述属性的最短字符串。


提示：

1 <= str1.length, str2.length <= 1000
str1 和 str2 都由小写英文字母组成。
"""


# https://blog.csdn.net/tham_/article/details/48718587

class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        # 回溯求最长公共子序列
        L = dp[-1][-1]
        print(L)
        res = set()
        i, j = m, n

        def backtrack(i, j, s):
            while i and j:
                if s1[i - 1] == s2[j - 1]:
                    s += s1[i - 1]
                    i -= 1
                    j -= 1
                else:
                    if dp[i - 1][j] > dp[i][j - 1]:
                        i -= 1
                    elif dp[i - 1][j] < dp[i][j - 1]:
                        j -= 1
                    else:
                        backtrack(i - 1, j, s)
                        backtrack(i, j - 1, s)
                        return
            res.add(s[::-1])

        backtrack(i, j, "")
        return res


if __name__ == '__main__':
    str1 = "ABCBDAB"
    str2 = "BDCABA"
    print(Solution().shortestCommonSupersequence(str1, str2))
