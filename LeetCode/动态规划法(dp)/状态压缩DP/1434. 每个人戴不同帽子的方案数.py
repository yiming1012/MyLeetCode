"""
总共有 n 个人和 40 种不同的帽子，帽子编号从 1 到 40 。

给你一个整数列表的列表 hats ，其中 hats[i] 是第 i 个人所有喜欢帽子的列表。

请你给每个人安排一顶他喜欢的帽子，确保每个人戴的帽子跟别人都不一样，并返回方案数。

由于答案可能很大，请返回它对 10^9 + 7 取余后的结果。

 

示例 1：

输入：hats = [[3,4],[4,5],[5]]
输出：1
解释：给定条件下只有一种方法选择帽子。
第一个人选择帽子 3，第二个人选择帽子 4，最后一个人选择帽子 5。
示例 2：

输入：hats = [[3,5,1],[3,5]]
输出：4
解释：总共有 4 种安排帽子的方法：
(3,5)，(5,3)，(1,3) 和 (1,5)
示例 3：

输入：hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
输出：24
解释：每个人都可以从编号为 1 到 4 的帽子中选。
(1,2,3,4) 4 个帽子的排列方案数为 24 。
示例 4：

输入：hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
输出：111
 

提示：

n == hats.length
1 <= n <= 10
1 <= hats[i].length <= 40
1 <= hats[i][j] <= 40
hats[i] 包含一个数字互不相同的整数列表。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-ways-to-wear-different-hats-to-each-other
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from collections import defaultdict


class Solution:
    def numberWays1(self, hats: List[List[int]]) -> int:
        # 让人戴帽子的嵌套列表 -> 把帽子送人的字典
        d = {k: set() for k in range(1, 41)}
        n = len(hats)
        for i in range(n):
            for hat in hats[i]:
                d[hat].add(i)

        # 构造 dp table
        cols = 2 ** n
        # 第 0 行，没有可用帽子时，方案数为 0
        dp = [[0] * cols for i in range(41)]
        # 没有可用帽子，但又不用送帽子，方案数为 1
        dp[0][0] = 1

        for i in range(1, 41):
            for j in range(cols):
                # 情况一：不送帽i
                dp[i][j] += dp[i - 1][j]
                # 情况二：送帽i给人k
                for k in d[i]:
                    # 当前戴帽状态 j 中，人k需要帽子
                    if j & (1 << k):
                        # 用 j ^ 1 << k 找到之前人k不戴帽子时的状态
                        dp[i][j] += dp[i - 1][j ^ 1 << k]

        return dp[-1][-1] % (10 ** 9 + 7)

    def numberWays2(self, hats: List[List[int]]) -> int:
        n = len(hats)
        # 初始化mp {帽子：[人1， 人2...],...}
        mp = defaultdict(list)
        for i in range(n):
            for j in range(len(hats[i])):
                mp[hats[i][j]].append(i)

        # 初始化dp[m + 1][2 ** n]
        m = 40
        dp = [[0] * (2 ** n) for _ in range(m + 1)]
        dp[0][0] = 1

        # 对于每顶帽子
        for i in range(1, m + 1):
            # 对于每种状态
            for j in range(2 ** n):
                # 没人戴帽子i
                dp[i][j] = dp[i - 1][j]
                # 有人k戴帽子i
                for k in mp[i]:
                    # 此状态下k戴着帽子
                    if j & (1 << k):
                        dp[i][j] += dp[i - 1][j - (1 << k)]
        return dp[-1][-1] % (10 ** 9 + 7)

    def numberWays3(self, hats: List[List[int]]) -> int:
        n = len(hats)
        dp = [[0] * (1 << n) for _ in range(41)]
        dp[0][0] = 1  #
        for i in range(1, 41):  # i: 第几顶帽子
            dp[i][:] = dp[i - 1][:]  # 这一步写成 dp[i] = dp[i-1]不对，具体原因我还没搞明白，路过的大佬帮忙解释一下？
            for j in range(n):  # j: 第几个人, [0, n-1]
                if i in hats[j]:
                    for state in range(1 << n):
                        if state & (1 << j) == 0:
                            dp[i][state | (1 << j)] += dp[i - 1][state]
        return dp[-1][(1 << n) - 1] % (10 ** 9 + 7)


if __name__ == '__main__':
    hats = [[3, 4], [4, 5], [5]]
    print(Solution().numberWays1(hats))
    print(Solution().numberWays2(hats))
    print(Solution().numberWays3(hats))
