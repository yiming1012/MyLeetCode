"""

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。



示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s):
        """
        思路：回溯法
        1. 每一位ip地址最大只有三个字符，0~255
        2. 总共分为四段
        3. 长度大于1的字符串，首位不能为零，str(int(p)) == p判断
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 4 or n > 12:
            return []

        def backtrack(s, tmp):
            if len(s) == 0 and len(tmp) == 4:
                res.append('.'.join(tmp))
                return
            if len(tmp) < 4:
                for i in range(min(3, len(s))):
                    p, n = s[:i + 1], s[i + 1:]
                    if p and 0 <= int(p) <= 255 and str(int(p)) == p:
                        backtrack(n, tmp + [p])

        res = []
        backtrack(s, [])
        return res


if __name__ == '__main__':
    s = "25525511135"
    print(Solution().restoreIpAddresses(s))
