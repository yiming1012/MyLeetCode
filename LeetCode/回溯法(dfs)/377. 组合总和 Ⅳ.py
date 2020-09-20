"""
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。
进阶：
如果给定的数组中含有负数会怎么样？
问题会产生什么变化？
我们需要在题目中添加什么限制来允许负数的出现？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def combinationSum1(self, nums: List[int], target: int) -> int:
        """
        思路：记忆化递归
        1. 普通递归超时，采用记忆化递归
        2. memo[target]=res，表示组合数的和为target时情况有res种
        @param nums:
        @param target:
        @return:
        """
        nums.sort()
        memo = {0: 1}

        def dfs(target):
            if target in memo:
                return memo[target]
            res = 0
            for i in range(len(nums)):
                if target - nums[i] >= 0:
                    res += dfs(target - nums[i])
            memo[target] = res
            return res

        return dfs(target)

    def combinationSum2(self, nums: List[int], target: int) -> int:
        """
        思路：动态规划法
        1. 一般来说，记忆化递归和动态规划法都可以相互转换
        @param nums:
        @param target:
        @return:
        """
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
                else:
                    break
        return dp[-1]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 9
    print(Solution().combinationSum1(nums, target))
    print(Solution().combinationSum2(nums, target))
