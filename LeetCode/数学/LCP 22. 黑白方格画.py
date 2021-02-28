"""
LCP 22. 黑白方格圆
小扣注意到秋日市集上有一个创作黑白方格画的摊位。摊主给每个顾客提供一个固定在墙上的白色画板，画板不能转动。画板上有 n * n 的网格。
绘画规则为，小扣可以选择任意多行以及任意多列的格子涂成黑色，所选行数、列数均可为 0。

小扣希望最终的成品上需要有 k 个黑色格子，请返回小扣共有多少种涂色方案。

注意：两个方案中任意一个相同位置的格子颜色不同，就视为不同的方案。

示例 1：

输入：n = 2, k = 2

输出：4

解释：一共有四种不同的方案：
第一种方案：涂第一列；
第二种方案：涂第二列；
第三种方案：涂第一行；
第四种方案：涂第二行。

示例 2：

输入：n = 2, k = 1

输出：0

解释：不可行，因为第一次涂色至少会涂两个黑格。

示例 3：

输入：n = 2, k = 4

输出：1

解释：共有 2*2=4 个格子，仅有一种涂色方案。

限制：

1 <= n <= 6
0 <= k <= n * n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ccw6C7
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def paintingPlan(self, n: int, k: int) -> int:
        """
        思路：模拟
            1. i和j分别表示行数和列数
            2. 判断i行格子数+j列格子数-i*j个重复的格子数是否等于k
            3. 如果i行j列满足条件，那么组合数为C(n,i)*C(n,j)
            4. 可提前将阶层算好存到数组中，计算时直接取，不必重复递归求阶层
        @param n:
        @param k:
        @return:
        """

        C = [[1] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n):
            for j in range(i):
                C[i + 1][j + 1] = C[i][j] + C[i][j + 1]

        res = 0
        if k == n * n:
            return 1
        for i in range(n + 1):
            for j in range(n + 1):
                if i * n + j * n - i * j == k:
                    res += C[n][i] * C[n][j]
        return res


if __name__ == '__main__':
    n = 2
    k = 2
    print(Solution().paintingPlan(n, k))
