"""
576. 出界的路径数
给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，你最多可以移动 N 次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。

 

示例 1：

输入: m = 2, n = 2, N = 2, i = 0, j = 0
输出: 6
解释:

示例 2：

输入: m = 1, n = 3, N = 3, i = 0, j = 1
输出: 12
解释:

 

说明:

球一旦出界，就不能再被移动回网格内。
网格的长度和高度在 [1,50] 的范围内。
N 在 [0,50] 的范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/out-of-boundary-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        思路：记忆化递归
        1. 记录每个位置和剩余次数对应的出圈次数
        @param m:
        @param n:
        @param maxMove:
        @param startRow:
        @param startColumn:
        @return:
        """
        pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(i, j, s):
            if s < 0: return 0
            if i < 0 or i == m or j < 0 or j == n: return 1
            ans = 0
            for dx, dy in pos:
                ans += dfs(i + dx, j + dy, s - 1)
                ans %= mod
            return ans

        res = dfs(startRow, startColumn, maxMove)
        dfs.cache_clear()
        return res % mod


if __name__ == '__main__':
    m = 2
    n = 2
    N = 2
    i = 0
    j = 0
    print(Solution().findPaths(m, n, N, i, j))
