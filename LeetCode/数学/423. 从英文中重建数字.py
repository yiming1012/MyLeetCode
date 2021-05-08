"""
423. 从英文中重建数字
给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。

注意:

输入只包含小写英文字母。
输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
输入字符串的长度小于 50,000。
示例 1:

输入: "owoztneoer"

输出: "012" (zeroonetwo)
示例 2:

输入: "fviefuro"

输出: "45" (fourfive)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reconstruct-original-digits-from-english
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        """
        思路：找到每个单词专属的字母就能找到对应单词的个数
        @param s:
        @return:
        """
        cnt = Counter(s)
        n0 = cnt['z']
        n2 = cnt['w']
        n4 = cnt['u']
        n6 = cnt['x']
        n8 = cnt['g']

        n5 = cnt['f'] - n4
        n1 = cnt['o'] - n0 - n2 - n4
        n3 = cnt['t'] - n2 - n8
        n9 = cnt['i'] - n6 - n5 - n8
        n7 = cnt['s'] - n6

        ns = (n0, n1, n2, n3, n4, n5, n6, n7, n8, n9)

        return "".join((str(i) * n for i, n in enumerate(ns)))