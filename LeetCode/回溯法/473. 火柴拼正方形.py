"""
还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。

输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。

示例 1:

输入: [1,1,2,2,2]
输出: true

解释: 能拼成一个边长为2的正方形，每边两根火柴。
示例 2:

输入: [3,3,3,3,4]
输出: false

解释: 不能用所有火柴拼成一个正方形。
注意:

给定的火柴长度和在 0 到 10^9之间。
火柴数组的长度不超过15。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matchsticks-to-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        s, n = sum(nums), len(nums)
        t = s // 4
        if len(nums) < 4 or s % 4:
            return False

        nums.sort(reverse=True)
        vis = [0] * n

        def dfs(curr, u, k):
            # 第几条边已经完成
            if u == 4:
                return True
                # 当前边的长度
            if curr == t:
                return dfs(0, u + 1, 0)

            # 用第k根火柴
            i = k
            while i < n:
                # 如果这根火柴已经被拼过或者加上当前边已构成的长度大于正方形边长，继续遍历下一条
                if vis[i] == 1 or curr + nums[i] > t:
                    i += 1
                    continue

                # 回溯
                vis[i] = 1
                if dfs(curr + nums[i], u, i + 1): return True
                vis[i] = 0

                # 当前边为0或目标边长
                if curr == 0 or curr + nums[i] == t:
                    return False

                # 如果不能拼成边长，跳过相同长度的火柴
                i += 1
                while i < n and nums[i - 1] == nums[i]:
                    i += 1
            return False

        return dfs(0, 0, 0)


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2]
    print(Solution().makesquare(nums))
