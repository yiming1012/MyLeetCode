'''

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        思路：双指针
        1. 主要在于优化
        2. 首先得排序
        3. if i>0 and nums[i]==nums[i-1]：continue
        4. 如果最小的三个数大于target，此时最接近target的数已存在
        5. 如果最大的三个数小于target，continue
        """
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            l, r = i + 1, n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            threeSum = nums[i] + nums[i + 1] + nums[i + 2]
            if threeSum >= target:
                if abs(threeSum - target) < abs(res - target):
                    res = threeSum
                    return res
            if nums[i] + nums[-1] + nums[-2] < target:
                res = nums[i] + nums[-1] + nums[-2]
                continue

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < target:
                    if abs(threeSum - target) < abs(res - target):
                        res = threeSum
                    l += 1
                    # 连续的数相等，则跳过
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif threeSum > target:
                    if abs(threeSum - target) < abs(res - target):
                        res = threeSum
                    r -= 1
                    # 连续的数相等，则跳过
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    return target
        return res


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution().threeSumClosest(nums, target))
