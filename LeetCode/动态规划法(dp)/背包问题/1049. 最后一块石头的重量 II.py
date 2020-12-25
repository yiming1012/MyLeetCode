"""
1049. 最后一块石头的重量 II
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。

 

示例：

输入：[2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
 

提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/last-stone-weight-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        思路：01背包问题
        1. 题目要求剩余的值最小，最好是选出一半的值，才能与剩余的石头碰撞后得到的值最小
        @param stones:
        @return:
        """
        total = sum(stones)
        target = total // 2
        dp = [0] * (target + 1)
        for v in stones:
            for i in range(target, v - 1, -1):
                dp[i] = max(dp[i], dp[i - v] + v)
        return total - 2 * dp[-1]


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeightII(stones))
