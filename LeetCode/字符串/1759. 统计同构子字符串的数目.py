"""
1759. 统计同构子字符串的数目
给你一个字符串 s ，返回 s 中 同构子字符串 的数目。由于答案可能很大，只需返回对 109 + 7 取余 后的结果。

同构字符串 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同构字符串。

子字符串 是字符串中的一个连续字符序列。



示例 1：

输入：s = "abbcccaa"
输出：13
解释：同构子字符串如下所列：
"a"   出现 3 次。
"aa"  出现 1 次。
"b"   出现 2 次。
"bb"  出现 1 次。
"c"   出现 3 次。
"cc"  出现 2 次。
"ccc" 出现 1 次。
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13
示例 2：

输入：s = "xy"
输出：2
解释：同构子字符串是 "x" 和 "y" 。
示例 3：

输入：s = "zzzzz"
输出：15


提示：

1 <= s.length <= 105
s 由小写字符串组成
"""
import itertools


class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10 ** 9 + 7
        arr = [(k, len(list(v))) for k, v in itertools.groupby(s)]
        res = 0
        for k, v in arr:
            res += (v + 1) * v // 2

        return res % mod


if __name__ == '__main__':
    s = "abbcccaa"
    print(Solution().countHomogenous(s))
