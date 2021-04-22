"""
1815. 得到新鲜甜甜圈的最多组数
有一个甜甜圈商店，每批次都烤 batchSize 个甜甜圈。这个店铺有个规则，就是在烤一批新的甜甜圈时，之前 所有 甜甜圈都必须已经全部销售完毕。给你一个整数 batchSize 和一个整数数组 groups ，数组中的每个整数都代表一批前来购买甜甜圈的顾客，其中 groups[i] 表示这一批顾客的人数。每一位顾客都恰好只要一个甜甜圈。

当有一批顾客来到商店时，他们所有人都必须在下一批顾客来之前购买完甜甜圈。如果一批顾客中第一位顾客得到的甜甜圈不是上一组剩下的，那么这一组人都会很开心。

你可以随意安排每批顾客到来的顺序。请你返回在此前提下，最多 有多少组人会感到开心。

 

示例 1：

输入：batchSize = 3, groups = [1,2,3,4,5,6]
输出：4
解释：你可以将这些批次的顾客顺序安排为 [6,2,4,5,1,3] 。那么第 1，2，4，6 组都会感到开心。
示例 2：

输入：batchSize = 4, groups = [1,3,2,5,2,2,1,6]
输出：4
 

提示：

1 <= batchSize <= 9
1 <= groups.length <= 30
1 <= groups[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-groups-getting-fresh-donuts
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import lru_cache
from typing import List


class Solution:
    def maxHappyGroups(self, b: int, g: List[int]) -> int:
        """
        常规做法：二进制枚举（超时）
        1. 本代码可帮助理解题目意思
        @param b:
        @param g:
        @return:
        """
        n = len(g)
        dp = [0] * (1 << n)
        for i in range(1 << n):
            s = 0
            for j in range(n):
                if i >> j & 1:
                    s += g[j]
            for j in range(n):
                if i & 1 << j == 0:
                    dp[i | (1 << j)] = max(dp[i | (1 << j)], dp[i] + int(s % b == 0))
        return dp[-1]



    def maxHappyGroups(self, b: int, g: List[int]) -> int:
        """
        如果用2进制枚举会超时，由于客户数量最多30组，采用31进制
        @param b:
        @param g:
        @return:
        """
        arr = [0] * b
        for gg in g:
            arr[gg % b] += 1
        t = 0
        for i in range(1, b):
            t += arr[i] * 31 ** i

        @lru_cache(None)
        def dfs(cur, t):
            if not t: return 0
            ans = 0
            for i in range(1, b):
                if (t // 31 ** i) % 31 > 0:
                    ans = max(ans, int(cur == 0) + dfs((cur + i) % b, t - 31 ** i))
            return ans

        dfs.cache_clear()
        return arr[0] + dfs(0, t)


if __name__ == '__main__':
    batchSize = 3
    groups = [1, 2, 3, 4, 5, 6]
    print(Solution().maxHappyGroups(batchSize, groups))
