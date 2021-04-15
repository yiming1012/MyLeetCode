"""
276. 栅栏涂色
有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，请你按下述规则为栅栏设计涂色方案：

每个栅栏柱可以用其中 一种 颜色进行上色。
相邻的栅栏柱 最多连续两个 颜色相同。
给你两个整数 k 和 n ，返回所有有效的涂色 方案数 。

 

示例 1：


输入：n = 3, k = 2
输出：6
解释：所有的可能涂色方案如上图所示。注意，全涂红或者全涂绿的方案属于无效方案，因为相邻的栅栏柱 最多连续两个 颜色相同。
示例 2：

输入：n = 1, k = 1
输出：1
示例 3：

输入：n = 7, k = 2
输出：42
 

提示：

1 <= n <= 50
1 <= k <= 105
题目数据保证：对于输入的 n 和 k ，其答案在范围 [0, 231 - 1] 内

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paint-fence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numWays1(self, n: int, k: int) -> int:
        def dfs(n):
            if n == 1: return k
            if n == 2: return k * k
            return (k - 1) * (dfs(n - 1) + dfs(n - 2))

        return dfs(n)

    def numWays2(self, n: int, k: int) -> int:
        if n == 1: return k
        if n == 2: return k * k
        dp = [1] * (n + 1)
        dp[1] = k
        dp[2] = k * k
        for i in range(3, n + 1):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
        return dp[-1]


if __name__ == '__main__':
    n = 3
    k = 2
    print(Solution().numWays1(n, k))
    print(Solution().numWays2(n, k))
