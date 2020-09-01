"""
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

 

示例 1：

输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
示例 2：

输入：K = 2, N = 6
输出：3
示例 3：

输入：K = 3, N = 14
输出：4
 

提示：

1 <= K <= 100
1 <= N <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-egg-drop
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def superEggDrop1(self, K: int, N: int) -> int:
        """
        dp[k][m] 的含义是k个鸡蛋 移动m次最多能够确定多少楼层
        这个角度思考
        dp[k][m] 最多能够确定的楼层数为L
        那么我选定第一个扔的楼层之后，我要么碎，要么不碎
        这就是把L分成3段
            1. 左边是碎的那段 长度是dp[k][m - 1]
            2. 右边是没碎的那段 长度是dp[k-1][m - 1] 因为已经碎了一个了
            3. 中间是我选定扔的楼层 是1
        所以递推公式:dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1
        """
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, K + 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] + 1
            if dp[i][K] >= N:
                return i

    def superEggDrop2(self, K: int, N: int) -> int:
        f = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            f[i][1] = i
        for i in range(1, K + 1):
            f[1][i] = 1
        for i in range(2, N + 1):
            for j in range(2, K + 1):
                f[i][j] = f[i][j - 1]
                for k in range(1, i + 1):
                    f[i][j] = min(f[i][j], max(f[k - 1][j - 1], f[i - k][j]) + 1)
        return f[N][K]


if __name__ == '__main__':
    K = 2
    N = 100
    print(Solution().superEggDrop1(K, N))
