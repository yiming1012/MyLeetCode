"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countSubstrings1(self, s: str) -> int:
        """
        思路：分别计算奇偶性
        @param s:
        @return:
        """
        n = len(s)
        res = 0
        for i in range(n):
            left, right = i, i
            # 奇数
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            # 偶数
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

    def countSubstrings2(self, s: str) -> int:
        """
        思路；将奇偶性合并在一起考虑，巧妙
        1. 将总长度扩大到2*N-1
        2. left = center//2 ，其中center的奇偶性对left没有影响
        3. right = left + center%2 ，当center为奇数时，right=left+1;当center为偶数时，right=left
        @param s:
        @return:
        """
        n = len(s)
        res = 0
        for i in range(2 * n - 1):
            left = i // 2
            right = left + i % 2
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res


if __name__ == '__main__':
    s = "aaaaa"
    print(Solution().countSubstrings1(s))
    print(Solution().countSubstrings2(s))
