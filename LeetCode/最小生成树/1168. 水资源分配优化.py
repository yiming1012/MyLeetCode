"""
村里面一共有 n 栋房子。我们希望通过建造水井和铺设管道来为所有房子供水。

对于每个房子 i，我们有两种可选的供水方案：

1. 一种是直接在房子内建造水井，成本为 wells[i]；
2. 另一种是从另一口井铺设管道引水，数组 pipes 给出了在房子间铺设管道的成本，
其中每个 pipes[i] = [house1, house2, cost] 代表用管道将 house1 和 house2 连接在一起的成本。当然，连接是双向的。
请你帮忙计算为所有房子都供水的最低总成本。

示例：


输入：n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
输出：3
解释：
上图展示了铺设管道连接房屋的成本。
最好的策略是在第一个房子里建造水井（成本为 1），然后将其他房子铺设管道连起来（成本为 2），所以总成本为 3。

提示：

1. 1 <= n <= 10000
2. wells.length == n
3. 0 <= wells[i] <= 10^5
4. 1 <= pipes.length <= 10000
5. 1 <= pipes[i][0], pipes[i][1] <= n
6. 0 <= pipes[i][2] <= 10^5
7. pipes[i][0] != pipes[i][1]
"""
from typing import List


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        for i, v in enumerate(wells):
            pipes.append([0, i + 1, v])

        parent = [i for i in range(n)]
        pipes.sort(key=lambda x: x[2])
        print(pipes)
        edge = 0
        res = 0

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v, w in pipes:
            x = find(u - 1)
            y = find(v - 1)
            if x != y:
                edge += 1
                parent[y] = x
                res += w
            if edge == n - 1:
                return res

        return res


if __name__ == '__main__':
    n = 3
    wells = [1, 2, 2]
    pipes = [[1, 2, 1], [2, 3, 1]]
    print(Solution().minCostToSupplyWater(n, wells, pipes))
