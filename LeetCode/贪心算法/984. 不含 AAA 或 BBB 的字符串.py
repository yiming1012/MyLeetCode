"""
984. 不含 AAA 或 BBB 的字符串
给定两个整数 A 和 B，返回任意字符串 S，要求满足：

S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母；
子串 'aaa' 没有出现在 S 中；
子串 'bbb' 没有出现在 S 中。
 

示例 1：

输入：A = 1, B = 2
输出："abb"
解释："abb", "bab" 和 "bba" 都是正确答案。
示例 2：

输入：A = 4, B = 1
输出："aabaa"
 

提示：

0 <= A <= 100
0 <= B <= 100
对于给定的 A 和 B，保证存在满足要求的 S。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-without-aaa-or-bbb
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        """
        思路：贪心算法
        1. 首先确定一个比较大的数a
        2. 如果a-b>0,先添加一个'a'，然后如果a,b都不为零，再分别填充'a'和'b'
        @param a:
        @param b:
        @return:
        """
        A = 'a'
        B = 'b'
        res = []
        if a < b:
            a, b = b, a
            A, B = B, A

        while a or b:
            if a - b:
                res.append(A)
                a -= 1
            if a:
                res.append(A)
                a -= 1
            if b:
                res.append(B)
                b -= 1
        return "".join(res)


if __name__ == '__main__':
    a, b = 1, 4
    print(Solution().strWithout3a3b(a, b))
