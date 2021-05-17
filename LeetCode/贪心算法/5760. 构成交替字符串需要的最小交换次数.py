"""
5760. 构成交替字符串需要的最小交换次数
给你一个二进制字符串 s ，现需要将其转化为一个 交替字符串 。请你计算并返回转化所需的 最小 字符交换次数，如果无法完成转化，返回 -1 。

交替字符串 是指：相邻字符之间不存在相等情况的字符串。例如，字符串 "010" 和 "1010" 属于交替字符串，但 "0100" 不是。

任意两个字符都可以进行交换，不必相邻 。

 

示例 1：

输入：s = "111000"
输出：1
解释：交换位置 1 和 4："111000" -> "101010" ，字符串变为交替字符串。
示例 2：

输入：s = "010"
输出：0
解释：字符串已经是交替字符串了，不需要交换。
示例 3：

输入：s = "1110"
输出：-1
 

提示：

1 <= s.length <= 1000
s[i] 的值为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        """
        思路：
        1. 遇到01交错字符串，无非就两种情况：
            1. 以0开头，如0101010
            2. 以1开头：如1010101
        @param s:
        @return:
        """
        a = s.count('1')
        b = s.count('0')
        if abs(a - b) > 1: return -1
        n = len(s)

        def cnt(e):
            a = b = 0
            for i in range(n):
                if i & 1 == 0 and s[i] != e:
                    a += 1
                if i & 1 and s[i] == e:
                    b += 1
            if a != b: return float('inf')
            return a if a == b else float('inf')

        ans = min(cnt('1'), cnt('0'))
        return ans if ans != float('inf') else -1


if __name__ == '__main__':
    s = "111000"
    print(Solution().minSwaps(s))
