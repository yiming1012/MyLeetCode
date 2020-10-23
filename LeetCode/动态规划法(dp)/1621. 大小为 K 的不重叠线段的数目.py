"""
给你一维空间的 n 个点，其中第 i 个点（编号从 0 到 n-1）位于 x = i 处，请你找到 恰好 k 个不重叠 线段且每个线段至少覆盖两个点的方案数。线段的两个端点必须都是 整数坐标 。这 k 个线段不需要全部覆盖全部 n 个点，且它们的端点 可以 重合。

请你返回 k 个不重叠线段的方案数。由于答案可能很大，请将结果对 109 + 7 取余 后返回。

 

示例 1：


输入：n = 4, k = 2
输出：5
解释：
如图所示，两个线段分别用红色和蓝色标出。
上图展示了 5 种不同的方案 {(0,2),(2,3)}，{(0,1),(1,3)}，{(0,1),(2,3)}，{(1,2),(2,3)}，{(0,1),(1,2)} 。
示例 2：

输入：n = 3, k = 1
输出：3
解释：总共有 3 种不同的方案 {(0,1)}, {(0,2)}, {(1,2)} 。
示例 3：

输入：n = 30, k = 7
输出：796297179
解释：画 7 条线段的总方案数为 3796297200 种。将这个数对 109 + 7 取余得到 796297179 。
示例 4：

输入：n = 5, k = 3
输出：7
示例 5：

输入：n = 3, k = 2
输出：1
 

提示：

2 <= n <= 1000
1 <= k <= n-1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-sets-of-k-non-overlapping-line-segments
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math


class Solution:
    def numberOfSets1(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        # dp[i][j][t] 表示区间[0,i]中取j段有几种取法
        # t=0 不取, t=1 取新一段, t=2 和前一段连起来
        dp = [[[0, 0, 0] for t in range(k + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][0][0] = 1
        for i in range(1, n):
            for j in range(1, min(i, k) + 1):
                # 当前不选，能构成j段的总数就是前面构成j的三种可能之和
                dp[i][j][0] = sum(dp[i - 1][j])
                # 当前选择，能够成新的一段，总数为前一段不选的三种可能之和
                dp[i][j][1] = sum(dp[i - 1][j - 1])
                # 当前选择，和前面连成一段，总数为前面一段构成j段
                dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]
        return sum(dp[n - 1][k]) % MOD

    def numberOfSets2(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        # 长度为k连续的线段中间添加k-1个点使得变成分开的k段
        # math.comb是python3.8的功能
        # return math.comb(n + k - 1, 2 * k) % mod


if __name__ == '__main__':
    n, k = 4, 2
    print(Solution().numberOfSets1(n, k))
    print(Solution().numberOfSets2(n, k))
