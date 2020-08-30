"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。
示例 2:

输入: "aba"

输出: False
示例 3:

输入: "abcabcabcabc"

输出: True

解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-substring-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def repeatedSubstringPattern1(self, s: str) -> bool:
        """
        思路：如果一个字符串由子串多次构成，可以模拟
        S = s * k , k=len(S) // len(s)
        @param s:
        @return:
        """
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                k = n // i
                if s == s[:i] * k:
                    return True
        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
        """
        标准KMP模板
        1. 先计算next数据
        2. 再比较两个字符串，不用回溯，时间复杂度O(N)
        @param s:
        @return:
        """

        def kmp(S, s):
            n = len(s)
            m = len(S)
            nex = [0] * n
            nex[0] = -1
            k = -1
            j = 0
            while j < n - 1:
                if k == -1 or s[k] == s[j]:
                    k += 1
                    j += 1
                    nex[j] = k
                else:
                    k = nex[k]
            # print(nex)

            i, j = 0, -1
            while i < m - 1:
                if S[i] == s[j] or j == -1:
                    i += 1
                    j += 1
                else:
                    j = nex[j]
                if j == n:
                    return True
            return False

        return kmp(s + s, s)

    def repeatedSubstringPattern3(self, s: str) -> bool:
        def kmp(pattern: str) -> bool:
            n = len(pattern)
            fail = [-1] * n
            for i in range(1, n):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1
            print(fail)
            return fail[n - 1] != -1 and n % (n - fail[n - 1] - 1) == 0

        return kmp(s)


if __name__ == '__main__':
    s = "abcabcabd"
    print(Solution().repeatedSubstringPattern1(s))
    print(Solution().repeatedSubstringPattern2(s))
    print(Solution().repeatedSubstringPattern3(s))
