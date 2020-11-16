"""
5551. 使字符串平衡的最少删除次数
给你一个字符串 s ，它仅包含字符 'a' 和 'b'​​​​ 。

你可以删除 s 中任意数目的字符，使得 s 平衡 。我们称 s 平衡的 当不存在下标对 (i,j) 满足 i < j 且 s[i] = 'b' 同时 s[j]= 'a' 。

请你返回使 s 平衡 的 最少 删除次数。



示例 1：

输入：s = "aababbab"
输出：2
解释：你可以选择以下任意一种方案：
下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。
示例 2：

输入：s = "bbaaaaabb"
输出：2
解释：唯一的最优解是删除最前面两个字符。


提示：

1 <= s.length <= 105
s[i] 要么是 'a' 要么是 'b'​ 。​
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        思路：
        1. 记录某个点左边和右边需要删除多少次
        2. 最后求两者和的最小值
        @param s:
        @return:
        """
        n = len(s)
        a, b = [0] * (n + 1), [0] * (n + 1)

        for i in range(n):
            a[i + 1] = a[i]
            b[n - i - 1] = b[n - i]
            if s[i] == "b":
                a[i + 1] += 1
            if s[n - i - 1] == "a":
                b[n - i - 1] += 1
        print(a, b)
        res = float('inf')
        for i in range(n):
            res = min(res, a[i] + b[i + 1])
        return res
