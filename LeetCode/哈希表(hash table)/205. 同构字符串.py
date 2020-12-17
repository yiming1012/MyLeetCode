"""
205. 同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/isomorphic-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # zip
    def isIsomorphic1(self, s: str, t: str) -> bool:
        word = zip(*set(zip(s, t)))
        for w in word:
            if len(w) != len(set(w)):
                return False
        return True
    # map
    def isIsomorphic2(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]

    # index
    def isIsomorphic3(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True

    # 双哈希
    def isIsomorphic4(self, s: str, t: str) -> bool:
        dic1 = dict()
        dic2 = dict()
        n = len(s)
        for i in range(n):
            if (s[i] in dic1 and dic1[s[i]] != t[i]) or (t[i] in dic2 and dic2[t[i]] != s[i]):
                return False
            dic1[s[i]] = t[i]
            dic2[t[i]] = s[i]
        return True


if __name__ == '__main__':
    s, t = "egg", "add"
    print(Solution().isIsomorphic1(s, t))
    print(Solution().isIsomorphic2(s, t))
    print(Solution().isIsomorphic3(s, t))
    print(Solution().isIsomorphic4(s, t))
