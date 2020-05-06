'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''
import os
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了72.64%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了14.68%的用户
        方法：利用第一个字符串遍历
        :param strs:
        :return:
        '''
        if len(strs) == 0:
            return ""

        a = strs[0]

        for i in range(len(a)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or a[i] != strs[j][i]:
                    return a[0:i] if i > 0 else ""

        return a

    def longestCommonPrefix2(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res) - 1]
            i += 1
        return res

    def longestCommonPrefix3(self, strs: List[str]) -> str:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了51.35%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了14.68%的用户
        利用zip 和 set
        【第一行】每次都取各个字符串的同一列字符，放进 set，set 中不会储存重复元素，所以长度为1代表各个字符都是相同的，此时 == 会让它变成 True
        【第二行】index 搜索第一个 0 的位置，0 与 False 在值上是等价的，相当于搜索第一个 False 的位置也就是公共前缀的长度
        :param strs:
        :return:
        '''
        s = ""
        print(zip(*strs))
        for i in zip(*strs):
            print(i)
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s

    def longestCommonPrefix4(self, strs: List[str]) -> str:
        '''
        执行用时 :60 ms, 在所有 Python3 提交中击败了9.25%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了14.68%的用户
        os自带模块
        :param strs:
        :return:
        '''
        return os.path.commonprefix(strs)





'''
1、通过数组里的第一个 去遍历后面的字符串 遇到不相同的就退出，否则返回第一个字符串
'''

if __name__ == '__main__':
    s = Solution()
    arr = ["flower", "flow", "flight"]
    print(s.longestCommonPrefix3(arr))
