'''

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        执行用时 :148 ms, 在所有 Python3 提交中击败了47.22%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了9.38%的用户
        :param nums:
        :param target:
        :return:
        '''
        n = len(nums)
        nums.sort()
        positive = float('inf')
        negative = -float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum > target:
                    positive = min(positive, three_sum - target)
                    right -= 1
                elif three_sum < target:
                    negative = max(negative, three_sum - target)
                    left += 1
                else:
                    return target
        # print(positive,negative)
        return target + positive if positive + negative < 0 else target + negative


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        执行用时 :132 ms, 在所有 Python3 提交中击败了59.59%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了9.38%的用户
        :param nums:
        :param target:
        :return:
        '''
        n=len(nums)
        nums.sort()
        res =sum(nums[:3])
        for i in range(n-2):
            left,right=i+1,n-1
            while left<right:
                three_sum=nums[i]+nums[left]+nums[right]
                if abs(three_sum-target)<abs(res-target):
                    res=three_sum
                if three_sum>target:
                    right-=1
                elif three_sum<target:
                    left+=1
                else:
                    return target
        return res
