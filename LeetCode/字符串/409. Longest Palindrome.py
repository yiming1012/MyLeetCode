'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes
that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了35.66%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.32%的用户
        :param s:
        :return:
        '''
        dic = collections.Counter(s)
        sum = 0
        for i in dic:
            if dic[i] % 2 == 1:
                dic[i] = dic[i] - 1
                sum = 1

        for i in dic:
            sum += dic[i]
        return sum

    def longestPalindrome2(self, s: str) -> int:
        '''
        执行用时 :56 ms, 在所有 Python3 提交中击败了13.26%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.32%的用户
        :param s:
        :return:
        '''
        dic = collections.Counter(s)
        sum = 0
        for i in dic:
            sum += dic[i] // 2 * 2
            if sum % 2 == 0 and dic[i] % 2 == 1:
                sum += 1
        return sum

    def longestPalindrome3(self, s: str) -> int:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了50.46%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.32%的用户
        关键点：只要得到的长度比原始长度短，说明有奇数个，返回值+1
        :param s:
        :return:
        '''
        dic = collections.Counter(s)
        sum = 0
        for i in dic:
            sum += dic[i] // 2 * 2

        return sum + 1 if len(s) > sum else sum

    def longestPalindrome4(self, s: str) -> int:
        '''
        执行用时 :32 ms, 在所有 Python3 提交中击败了86.43%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.32%的用户
        方法：如果为奇数，总长度-1，如"abcd",长度为4-3=1
        :param s:
        :return:
        '''
        return len(s) - max(0, sum([s.count(i) % 2 for i in set(s)]) - 1)


if __name__ == '__main__':
    ss = "abccccdd"
    s = Solution()
    print(s.longestPalindrome(ss))
