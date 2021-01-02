"""
1247. 交换字符使得字符串相同
有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，你需要通过「交换字符」的方式使这两个字符串相同。

每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。

交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[j]。

最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。

 

示例 1：

输入：s1 = "xx", s2 = "yy"
输出：1
解释：
交换 s1[0] 和 s2[1]，得到 s1 = "yx"，s2 = "yx"。
示例 2：

输入：s1 = "xy", s2 = "yx"
输出：2
解释：
交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。
交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。
注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。
示例 3：

输入：s1 = "xx", s2 = "xy"
输出：-1
示例 4：

输入：s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
输出：4
 

提示：

1 <= s1.length, s2.length <= 1000
s1, s2 只包含 'x' 或 'y'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-swaps-to-make-strings-equal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import Counter


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """
        思路：贪心算法
        1. 仅仅看('x', 'y')和('y', 'x')组合的个数，只要有单独一个为奇数就不行，两个都为奇数可以
        @param s1:
        @param s2:
        @return:
        """
        arr = [(x, y) for x, y in zip(s1, s2) if x != y]
        print(arr)
        dic = Counter(arr)
        res = 0
        res += dic[('x', 'y')] // 2 + dic[('y', 'x')] // 2
        if dic[('x', 'y')] % 2 == 0 and dic[('y', 'x')] % 2 == 0:
            return res
        elif dic[('x', 'y')] % 2 == 1 and dic[('y', 'x')] % 2 == 1:
            res += 2
            return res
        return -1


if __name__ == '__main__':
    s1 = "xx"
    s2 = "yy"
    print(Solution().minimumSwap(s1, s2))
