"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        思路：动态规划法
        1. 首先对第一行第一列初始化，注意如果p的首字符为*，dp对应位置为True
        2. 状态转移方程分两种情况：
         1) p[i]=='*': dp[i + 1][j + 1] = dp[i][j + 1] or dp[i + 1][j]
         2) p[i] == '?' or p[i] == s[j]: dp[i + 1][j + 1] = dp[i][j]
        """
        m, n = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(n):
            if p[i] == '*':
                dp[i + 1][0] = dp[i][0]
        for i in range(n):
            for j in range(m):
                if p[i] == '*':
                    dp[i + 1][j + 1] = dp[i][j + 1] or dp[i + 1][j]
                elif p[i] == '?' or p[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j]

        return dp[-1][-1]


if __name__ == '__main__':
    s = "acdcb"
    p = "a*c?b"
    print(Solution().isMatch(s, p))
