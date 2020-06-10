"""
在一个小城市里，有 m 个房子排成一排，你需要给每个房子涂上 n 种颜色之一（颜色编号为 1 到 n ）。有的房子去年夏天已经涂过颜色了，所以这些房子不需要被重新涂色。

我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 houses = [1,2,2,3,3,2,1,1] ，它包含 5 个街区  [{1}, {2,2}, {3,3}, {2}, {1,1}] 。）

给你一个数组 houses ，一个 m * n 的矩阵 cost 和一个整数 target ，其中：

houses[i]：是第 i 个房子的颜色，0 表示这个房子还没有被涂色。
cost[i][j]：是将第 i 个房子涂成颜色 j+1 的花费。
请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成 target 个街区。如果没有可用的涂色方案，请返回 -1 。

 

示例 1：

输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：9
解释：房子涂色方案为 [1,2,2,1,1]
此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。
示例 2：

输入：houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：11
解释：有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。
示例 3：

输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
输出：5
示例 4：

输入：houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
输出：-1
解释：房子已经被涂色并组成了 4 个街区，分别是 [{3},{1},{2},{3}] ，无法形成 target = 3 个街区。
 

提示：

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paint-house-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # 生成dp状态数组：dp[房子][颜色][街区]
        dp = [[[float('inf')] * (target + 1) for _ in range(n)] for _ in range(m)]
        print(dp)
        # 初始化dp状态
        if houses[0]:
            dp[0][houses[0] - 1][1] = 0
        else:
            for j in range(n):
                dp[0][j][1] = cost[0][j]

        # 开始动态规划
        for i in range(1, m):
            for j in range(n):
                for k in range(1, target + 1):

                    # 当前颜色已确定 且 （houses[i] - 1 != j），因此状态不可达，continue掉
                    if houses[i] > 0 and houses[i] - 1 != j:
                        continue

                    # 当前房子需要的花费
                    c = 0 if houses[i] > 0 else cost[i][j]

                    # 从前一个状态转移过来：1,2
                    # 1. 和前一个房子颜色相同
                    m = dp[i - 1][j][k]
                    # 2. 和前一个房子颜色不同
                    tmp = [dp[i - 1][x][k - 1] for x in range(n) if x != j]

                    m = min(m, *tmp)
                    dp[i][j][k] = m + c

        ans = min([dp[-1][j][target] for j in range(n)])
        if ans == float('inf'): ans = -1
        return ans
