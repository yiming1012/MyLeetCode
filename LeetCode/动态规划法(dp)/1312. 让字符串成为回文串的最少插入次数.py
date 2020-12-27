"""
1312. 让字符串成为回文串的最少插入次数
给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。

请你返回让 s 成为回文串的 最少操作次数 。

「回文串」是正读和反读都相同的字符串。

 

示例 1：

输入：s = "zzazz"
输出：0
解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
示例 2：

输入：s = "mbadm"
输出：2
解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
示例 3：

输入：s = "leetcode"
输出：5
解释：插入 5 个字符后字符串变为 "leetcodocteel" 。
示例 4：

输入：s = "g"
输出：0
示例 5：

输入：s = "no"
输出：1
 

提示：

1 <= s.length <= 500
s 中所有字符都是小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minInsertions1(self, s: str) -> int:
        """
        思路：动态规划法
        1. s翻转后s_，两者求最长公共子序列，剩余的则是要插入的
        @param s:
        @return:
        """
        n = len(s)
        s_ = s[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                if s[i] == s_[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return n - dp[-1][-1]


    def minInsertions2(self, s: str) -> int:
        """
        思路：区间dp
        @param s:
        @return:
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for span in range(2, n + 1):
            for l in range(n - span + 1):
                r = l + span - 1
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1]
                else:
                    dp[l][r] = min(dp[l + 1][r], dp[l][r - 1]) + 1
        return dp[0][n - 1]


if __name__ == '__main__':
    s = "abac"
    print(Solution().minInsertions(s))
