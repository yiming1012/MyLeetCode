"""
1771. 由子序列构造的最长回文串的长度
给你两个字符串 word1 和 word2 ，请你按下述方法构造一个字符串：

从 word1 中选出某个 非空 子序列 subsequence1 。
从 word2 中选出某个 非空 子序列 subsequence2 。
连接两个子序列 subsequence1 + subsequence2 ，得到字符串。
返回可按上述方法构造的最长 回文串 的 长度 。如果无法构造回文串，返回 0 。

字符串 s 的一个 子序列 是通过从 s 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。

回文串 是正着读和反着读结果一致的字符串。



示例 1：

输入：word1 = "cacb", word2 = "cbba"
输出：5
解释：从 word1 中选出 "ab" ，从 word2 中选出 "cba" ，得到回文串 "abcba" 。
示例 2：

输入：word1 = "ab", word2 = "ab"
输出：3
解释：从 word1 中选出 "ab" ，从 word2 中选出 "a" ，得到回文串 "aba" 。
示例 3：

输入：word1 = "aa", word2 = "bb"
输出：0
解释：无法按题面所述方法构造回文串，所以返回 0 。


提示：

1 <= word1.length, word2.length <= 1000
word1 和 word2 由小写英文字母组成
"""


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        """
        区间dp模板
        @param word1:
        @param word2:
        @return:
        """
        m, n = len(word1), len(word2)
        S = word1 + word2
        N = len(S)
        dp = [[0] * N for _ in range(N)]
        res = 0
        for span in range(1, N + 1):
            for left in range(N - span + 1):
                right = left + span - 1
                if span == 1:
                    dp[left][right] = 1
                else:
                    dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])
                    if S[left] == S[right]:
                        dp[left][right] = dp[left + 1][right - 1] + 2
                        if left < m <= right:
                            res = max(res, dp[left][right])
        return res


if __name__ == '__main__':
    word1 = "cacb"
    word2 = "cbba"
    print(Solution().longestPalindrome(word1, word2))
