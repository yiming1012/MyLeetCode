'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        if m < n:
            return -1
        for i in range(m):
            if haystack[i:i + n] == needle:
                return i
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        '''
        执行用时 :32 ms, 在所有 Python3 提交中击败了88.94%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.05%的用户
        :param haystack:
        :param needle:
        :return:
        '''
        return haystack.find(needle)


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    s = Solution()
    print(s.strStr(haystack, needle))
