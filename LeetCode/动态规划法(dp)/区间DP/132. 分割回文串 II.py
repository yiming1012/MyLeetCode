"""
132. 分割回文串 II
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。

返回符合要求的 最少分割次数 。

 

示例 1：

输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
示例 2：

输入：s = "a"
输出：0
示例 3：

输入：s = "ab"
输出：1
 

提示：

1 <= s.length <= 2000
s 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for span in range(2, n + 1):
            for i in range(n - span + 1):
                j = i + span - 1
                dp[i][j] = dp[i + 1][j - 1] if s[i] == s[j] else False

        f = [float('inf')] * n
        for i in range(n):
            if dp[0][i]:
                f[i] = 0
                continue
            for j in range(i):
                if dp[j + 1][i]:
                    f[i] = min(f[i], f[j] + 1)

        return f[-1]


if __name__ == '__main__':
    s = "aab"
    print(Solution().minCut(s))
