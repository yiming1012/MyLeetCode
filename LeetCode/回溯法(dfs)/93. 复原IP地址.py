"""

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。



示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        def dfs(path,cur):
            for i in range(1,4):
                if s[cur:cur+i]







if __name__ == '__main__':
    s = "25525511135"
    print(Solution().restoreIpAddresses(s))


