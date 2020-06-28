'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了97.88%的用户
        内存消耗 :14.2 MB, 在所有 Python3 提交中击败了19.73%的用户
        :param nums:
        :return:
        '''
        maxValue = sumValue = nums[0]
        i = 1
        while i < len(nums):
            if sumValue <= 0:
                sumValue = nums[i]
            else:
                sumValue += nums[i]
            i += 1

            if sumValue > maxValue:
                maxValue = sumValue
        return maxValue


    def maxSubArray2(self, nums: List[int]) -> int:
        '''
        如果前面的数之和小于0，那么与后面的数相加，只会更小。
        所以，当前面的presum小于0时，presum=num，大于0则继续相加
        每次计算最大值
        :param nums:
        :return:
        '''
        res = nums[0]
        presum = 0
        for num in nums:
            if presum < 0:
                presum = num
            else:
                presum += num
            if presum > res:
                res = presum

        return res


'''
此题的关键在于：前面的数之和sum必须大于0，才能与接下来的数字相加，否则将sum=nums[i]
'''
if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    res = s.maxSubArray(arr)
    print(res)
