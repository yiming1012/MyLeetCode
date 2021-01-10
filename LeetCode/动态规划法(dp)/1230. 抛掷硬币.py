"""
1230. 抛掷硬币
有一些不规则的硬币。在这些硬币中，prob[i] 表示第 i 枚硬币正面朝上的概率。

请对每一枚硬币抛掷 一次，然后返回正面朝上的硬币数等于 target 的概率。



示例 1：

输入：prob = [0.4], target = 1
输出：0.40000
示例 2：

输入：prob = [0.5,0.5,0.5,0.5,0.5], target = 0
输出：0.03125


提示：

1 <= prob.length <= 1000
0 <= prob[i] <= 1
0 <= target <= prob.length
如果答案与标准答案的误差在 10^-5 内，则被视为正确答案。
"""
from functools import reduce
from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """
        思路：动态规划法
        @param prob:
        @param target:
        @return:
        """
        if target == 0:
            return reduce(lambda x, y: x * y, [1 - v for v in prob])
        n = len(prob)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[1][0] = 1 - prob[0]
        dp[1][1] = prob[0]
        for i in range(2, n + 1):
            v = prob[i - 1]
            dp[i][0] = dp[i - 1][0] * (1 - v)
            for j in range(1, min(i, target) + 1):
                dp[i][j] = dp[i - 1][j] * (1 - v) + dp[i - 1][j - 1] * v
        return dp[-1][-1]


if __name__ == '__main__':
    prob = [0.4]
    target = 1
    print(Solution().probabilityOfHeads(prob, target))
