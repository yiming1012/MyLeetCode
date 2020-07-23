"""

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。



示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""
from typing import List


class Solution:
    def restoreIpAddresses1(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []

        def dfs(path, ss, cur):
            if len(path) == 4 and cur >= n:
                res.append(",".join(path))
                return
            for i in range(1, 4):
                sub = s[cur:cur + i + 1]
                nex = s[cur+i:]

                if str(int(sub)) == sub and int(sub) < 256:
                    dfs(path + [sub], nex, cur + i + 1)

        res = []
        dfs([], 0)
        print(res)
        return res

    def restoreIpAddresses2(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []

        def backtrack(s, tmp):
            if len(s) == 0 and len(tmp) == 4:
                self.res.append('.'.join(tmp))
                return
            if len(tmp) < 4:
                for i in range(min(3, len(s))):
                    p, n = s[:i + 1], s[i + 1:]
                    if p and 0 <= int(p) <= 255 and str(int(p)) == p:
                        backtrack(n, tmp + [p])

        backtrack(s, [])
        return self.res


if __name__ == '__main__':
    s = "25525511135"
    print(Solution().restoreIpAddresses1(s))
    print(Solution().restoreIpAddresses2(s))
