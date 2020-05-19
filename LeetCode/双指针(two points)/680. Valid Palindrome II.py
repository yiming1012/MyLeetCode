"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        执行用时 :112 ms, 在所有 Python3 提交中击败了72.38%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了36.36%的用户
        思路：双指针
        1、利用left和right两个指针从首尾遍历，如果相同，则同时移动两个指针
        2、当不相同时，说明必须删除一个，要么left，要么right
        3、Python3中判断是否是回文：s==s[::-1]
        """
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return s[left:right] == s[left:right][::-1] or s[left + 1:right + 1] == s[left + 1:right + 1][::-1]
        return True

    def validPalindrome2(self, s: str) -> bool:
        """
        改进：利用lambda
        """
        left, right = 0, len(s) - 1
        isPalindrome = lambda x: x == x[::-1]
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left:right]) or isPalindrome(s[left + 1:right + 1])
        return True


if __name__ == '__main__':
    a = "abcbca"
    print(Solution().validPalindrome(a))
