"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        思路：动态规划法
        1. 状态转移方程：dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        """
        n = len(cost)
        pre, cur = 0, 0
        for i in range(2, n + 1):
            pre, cur = cur, min(pre + cost[i - 2], cur + cost[i - 1])
        return cur

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        """
        1. 状态转移方程：pre, cur = cur, min(pre, cur) + cost[i]
        """
        pre, cur = cost[0], cost[1]
        for i in range(2, len(cost)):
            pre, cur = cur, min(pre, cur) + cost[i]
        return min(pre, cur)


if __name__ == '__main__':
    cost = [10, 15, 20]
    print(Solution().minCostClimbingStairs(cost))
    print(Solution().minCostClimbingStairs2(cost))
