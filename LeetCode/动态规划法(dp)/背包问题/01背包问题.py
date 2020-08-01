"""
// 初始赋值操作
value = new int[]{1500, 3000, 2000};
weight = new int[]{1, 4, 3};
c = 4;
n = 3;
"""


class Solution:
    def knapsack1(self, value, weight, target):
        """
        1. 每个物品可以选择放或不放
        2. dp[i][j]:装入第i个物品，背包容量为j时，获得的最大价值
            不放：dp[i][j]=dp[i-1][j]
            放：dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
        """
        m, n = len(value), target
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= weight[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
        return dp[-1][-1]

    def knapsack2(self, value, weight, target):
        """
        状态压缩：一维dp
        1. 由于dp[i-1][j]用的是上一层的数据，一维时，如果从前往后遍历，dp[j-v[i]]就已经是本层更新后的数据
        2. 怎么样才能等价于第i-1层呢？
            从大到小遍历。因为在计算dp[j]的时候，本层的dp[j-v[i]]还没有算过,此时dp[j-v[i]]使用的是上层的结果。
        """
        m, n = len(value), target
        dp = [0] * (n + 1)
        # dp[i]:装入第i个物品，背包容量为j时，获得的最大价值
        for i in range(1, m + 1):
            for j in range(target, weight[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])
        return dp[-1]


if __name__ == '__main__':
    value = [1500, 3000, 2000, 2000]
    weight = [1, 4, 3, 1]
    target = 4
    print(Solution().knapsack1(value, weight, target))
    print(Solution().knapsack2(value, weight, target))
