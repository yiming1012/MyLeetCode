"""
1140. 石子游戏 II
亚历克斯和李继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。

亚历克斯和李轮流进行，亚历克斯先开始。最初，M = 1。

在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。

游戏一直持续到所有石子都被拿走。

假设亚历克斯和李都发挥出最佳水平，返回亚历克斯可以得到的最大数量的石头。



示例：

输入：piles = [2,7,9,4,4]
输出：10
解释：
如果亚历克斯在开始时拿走一堆石子，李拿走两堆，接着亚历克斯也拿走两堆。在这种情况下，亚历克斯可以拿到 2 + 4 + 4 = 10 颗石子。
如果亚历克斯在开始时拿走两堆石子，那么李就可以拿走剩下全部三堆石子。在这种情况下，亚历克斯可以拿到 2 + 7 = 9 颗石子。
所以我们返回更大的 10。


提示：

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4
"""
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        # 数据规模与记忆化
        n, memo = len(piles), dict()

        # s[i] 表示第 i 堆石子到最后一堆石子的总石子数
        s = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            s[i] = s[i + 1] + piles[i]

        # dfs(i, M) 表示从第 i 堆石子开始取，最多能取 M 堆石子所能得到的最优值
        def dfs(i, M):
            # 如果已经搜索过，直接返回
            if (i, M) in memo:
                return memo[(i, M)]
            # 溢出拿不到任何石子
            if i >= n:
                return 0
            # 如果剩余堆数小于等于 2M， 那么可以全拿走
            if i + M * 2 >= n:
                return s[i]
            # 枚举拿 x 堆的最优值
            best = 0
            for x in range(1, M * 2 + 1):
                # 剩余石子减去对方最优策略
                best = max(best, s[i] - dfs(i + x, max(x, M)))
            # 记忆化
            memo[(i, M)] = best
            return best

        return dfs(0, 1)


if __name__ == '__main__':
    piles = [2, 7, 9, 4, 4]
    print(Solution().stoneGameII(piles))
