"""
面试题 01.05. 一次编辑
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

 

示例 1:

输入:
first = "pale"
second = "ple"
输出: True
 

示例 2:

输入:
first = "pales"
second = "pal"
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-away-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        """
        思路：遇到不同，比较后面字符串
        @param first:
        @param second:
        @return:
        """
        m, n = len(first), len(second)
        if abs(m - n) > 1:
            return False
        if m > n:
            m, n = n, m
            first, second = second, first

        i, j = 0, 0
        for i in range(m):
            if first[i] == second[i]:
                continue
            return first[i + 1:] == second[i + 1:] or first[i:] == second[i + 1:]
        return True