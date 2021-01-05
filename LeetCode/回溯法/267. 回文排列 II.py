"""
267. 回文排列 II
给定一个字符串 s ，返回其通过重新排列组合后所有可能的回文字符串，并去除重复的组合。

如不能形成任何回文排列时，则返回一个空列表。

示例 1：

输入: "aabb"
输出: ["abba", "baab"]
示例 2：

输入: "abc"
输出: []

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import Counter
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        arr = Counter(s)
        half = []
        odd = []
        for k, v in arr.items():
            if v & 1:
                odd.append(k)
            half.extend([k] * (v // 2))
            if len(odd) > 1:
                return []
        # 对key进行全排列
        half.sort()
        n = len(half)
        res = []
        visited = set()

        def permutation(a):
            if len(a) == n:
                res.append(a.copy())
                return
            for i in range(n):
                if i > 0 and half[i] == half[i - 1] and i - 1 not in visited: continue
                if i not in visited:
                    visited.add(i)
                    permutation(a + [half[i]])
                    visited.remove(i)

        permutation([])

        ans = set()
        for p in res:
            tmp = p + odd + p[::-1]
            ans.add("".join(tmp))
        return sorted(ans)


if __name__ == '__main__':
    s = "aabb"
    print(Solution().generatePalindromes(s))
