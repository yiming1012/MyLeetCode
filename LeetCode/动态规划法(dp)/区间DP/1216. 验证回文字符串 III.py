"""
1216. 验证回文字符串 III
给出一个字符串 s 和一个整数 k，请你帮忙判断这个字符串是不是一个「K 回文」。

所谓「K 回文」：如果可以通过从字符串中删去最多 k 个字符将其转换为回文，那么这个字符串就是一个「K 回文」。

 

示例：

输入：s = "abcdeca", k = 2
输出：true
解释：删除字符 “b” 和 “e”。
 

提示：

1 <= s.length <= 1000
s 中只含有小写英文字母
1 <= k <= s.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        思路：区间dp
        @param s:
        @param k:
        @return:
        """
        n = len(s)
        dp = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for span in range(2, n + 1):
            for left in range(n - span + 1):
                right = left + span - 1
                if span == 2:
                    dp[left][right] = 0 if s[left] == s[right] else 1
                    continue
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1]
                else:
                    dp[left][right] = min(dp[left + 1][right], dp[left][right - 1]) + 1
        return dp[0][-1] <= k


if __name__ == '__main__':
    s = "abcdeca"
    k = 2
    print(Solution().isValidPalindrome(s, k))
