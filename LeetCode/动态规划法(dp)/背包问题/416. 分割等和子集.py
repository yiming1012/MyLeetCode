"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def canPartition1(self, nums: List[int]) -> bool:
        """
        思路：01背包问题
        """
        n = len(nums)
        if n < 2:
            return False
        if sum(nums) & 1:
            return False
        target = sum(nums) // 2
        dp = [0] * (target + 1)

        for i in range(1, n + 1):
            for j in range(target, nums[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i - 1]] + nums[i - 1])
                if dp[j] == target:
                    return True
        return False

    def canPartition2(self, nums: List[int]) -> bool:
        """
        思路：01背包问题
        """
        n = len(nums)
        if n < 2:
            return False
        if sum(nums) & 1:
            return False
        target = sum(nums) // 2
        flag = 0

        def dfs(index, s):
            nonlocal flag
            if s == target:
                flag = 1
                return

            for i in range(index, n):
                if s + nums[i] <= target:
                    dfs(i + 1, s + nums[i])
                if flag == 1:
                    return

        dfs(0, 0)
        return flag == 1


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    print(Solution().canPartition1(nums))
    print(Solution().canPartition2(nums))
