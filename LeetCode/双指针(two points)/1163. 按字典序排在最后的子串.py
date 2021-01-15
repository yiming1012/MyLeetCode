"""
1163. 按字典序排在最后的子串
给你一个字符串 s，找出它的所有子串并按字典序排列，返回排在最后的那个子串。



示例 1：

输入："abab"
输出："bab"
解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是 "bab"。
示例 2：

输入："leetcode"
输出："tcode"


提示：

1 <= s.length <= 4 * 10^5
s 仅含有小写英文字符。
"""


class Solution:
    def lastSubstring(self, s: str) -> str:
        """
        思路：比较字典序
        @param s:
        @return:
        """
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l:] < s[r:]:
                l += 1
            else:
                r -= 1
        return s[l:]


if __name__ == '__main__':
    s = "leetcode"
    print(Solution().lastSubstring(s))

