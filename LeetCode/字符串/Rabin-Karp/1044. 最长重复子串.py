"""
1044. 最长重复子串
给出一个字符串 S，考虑其所有重复子串（S 的连续子串，出现两次或多次，可能会有重叠）。

返回任何具有最长可能长度的重复子串。（如果 S 不含重复子串，那么答案为 ""。）

 

示例 1：

输入："banana"
输出："ana"
示例 2：

输入："abcd"
输出：""
 

提示：

2 <= S.length <= 10^5
S 由小写英文字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-duplicate-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        nums = [ord(c) - ord('a') + 1 for c in s]
        P, Q = 131, 2 ** 64

        def check(L):
            visited = set()
            M = P ** L % Q
            pre = 0
            for i in range(L):
                pre = (pre * P + nums[i]) % Q
            visited.add(pre)
            for i in range(L, n):
                pre = (pre * P + nums[i] - nums[i - L] * M) % Q
                if pre in visited:
                    return i - L + 1
                visited.add(pre)
            return -1

        n = len(s)
        l, r = 0, n
        res = -1
        while l < r:
            mid = l + (r - l + 1) // 2
            index = check(mid)
            if index != -1:
                l = mid
                res = index
            else:
                r = mid - 1
        # print(l,r)
        return s[res:res + l] if res != -1 else ""


if __name__ == '__main__':
    S = "anana"
    print(Solution().longestDupSubstring(S))
