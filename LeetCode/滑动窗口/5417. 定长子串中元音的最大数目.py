"""
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）。



示例 1：

输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。
示例 2：

输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。
示例 3：

输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
示例 4：

输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。
示例 5：

输入：s = "tryhard", k = 4
输出：1


提示：

1 <= s.length <= 10^5
s 由小写英文字母组成
1 <= k <= s.length
"""
import collections


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        思路：滑动窗口+dict
        """
        aa = "aeiou"
        dic = collections.defaultdict(lambda: 0)
        res = float('-inf')
        for i, c in enumerate(s):
            dic[c] += 1
            if i >= k - 1:
                count = 0
                for j in aa:
                    count += dic[j]
                res = max(res, count)
                dic[s[i - k + 1]] -= 1
        return res

    def maxVowels2(self, s: str, k: int) -> int:
        """
        思路：滑动窗口优化
        1. 先统计前k个字符中每个元音的个数
        2. 后面将k长度的窗口向后滑动[i,i+k-1]，如果i+k-1出为元音，cnt+=1，如果i处为元音，cnt-=1
        3. 如果i+k==len(s)，遍历结束
        """
        v = {'a', 'e', 'i', 'o', 'u'}
        vcnt = 0
        for i in range(k):
            if s[i] in v:
                # 先初始化计算[0,k]窗口的元音字母个数
                vcnt += 1
        res = vcnt
        for b in range(len(s)):
            e = b + k
            if e >= len(s):
                break
            if s[e] in v:
                # 更新新的右边界的值
                vcnt += 1
            if s[b] in v:
                # 去除旧的左边界的值
                vcnt -= 1
            res = max(res, vcnt)
        return res
