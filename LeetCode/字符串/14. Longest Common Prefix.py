"""
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

"""
import os
from typing import List


class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        """
        思路：字符串通过ASCII码比较大小
        :param strs:
        :return:
        """
        if not strs:
            return ""

        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        """
        思路：Trie Tree

        """
        if not strs:
            return ''

            # 构建字典树
        root = {}
        for word in strs:
            if not word:  # 处理空字符串
                return ''
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = '#'  # 结束标志
        print(root)

        res, node = '', root
        while node != {'#': '#'}:  # 注意判断结束条件
            if len(node) == 1:
                char = str(*node)  # 字典中只有一个 key 时，可以使用解包操作
                res += char
                node = node[char]
            else:
                return res
        return res

    def longestCommonPrefix3(self, strs: List[str]) -> str:
        """
        思路：利用zip 和 set
        【第一行】每次都取各个字符串的同一列字符，放进 set，set 中不会储存重复元素，所以长度为1代表各个字符都是相同的，此时 == 会让它变成 True
        【第二行】index 搜索第一个 0 的位置，0 与 False 在值上是等价的，相当于搜索第一个 False 的位置也就是公共前缀的长度
        :param strs:
        :return:
        """
        res = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                res += i[0]
            else:
                break
        return res

    def longestCommonPrefix4(self, strs: List[str]) -> str:
        """
        执行用时 :60 ms, 在所有 Python3 提交中击败了9.25%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了14.68%的用户
        os自带模块
        :param strs:
        :return:
        """
        return os.path.commonprefix(strs)


"""
1、通过数组里的第一个 去遍历后面的字符串 遇到不相同的就退出，否则返回第一个字符串
"""

if __name__ == '__main__':
    s = Solution()
    arr = ["flower", "flow", "flight"]
    print(s.longestCommonPrefix1(arr))
    print(s.longestCommonPrefix2(arr))
    print(s.longestCommonPrefix3(arr))
    print(s.longestCommonPrefix4(arr))
