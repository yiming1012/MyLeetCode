'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        执行用时 :6280 ms, 在所有 Python3 提交中击败了5.00%的用户
        内存消耗 :14.7 MB, 在所有 Python3 提交中击败了5.40%的用户
        时间复杂度：O(n**2)
        :param nums:
        :return:
        '''
        for i, num in enumerate(nums):
            if i not in nums:
                return i
        return i + 1

    def missingNumber2(self, nums: List[int]) -> int:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了97.19%的用户
        内存消耗 :14.6 MB, 在所有 Python3 提交中击败了5.40%的用户
        思路：求出本该存在时的sum,减去现在list中的sum
        注意：有溢出风险
        :param nums:
        :return:
        '''
        n = len(nums) + 1
        return n * (n - 1) // 2 - sum(nums)

    def missingNumber3(self, nums: List[int]) -> int:
        '''
        执行用时 :68 ms, 在所有 Python3 提交中击败了67.26%的用户
        内存消耗 :14.7 MB, 在所有 Python3 提交中击败了5.40%的用户
        思路：
        1、增加-1
        2、遍历时使index和value的值相等，当等-1时跳过
        :param nums:
        :return:
        '''
        nums.append(-1)
        for i in range(len(nums)):
            while nums[i] != -1 and i != nums[i]:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]

        return nums.index(-1)

    def missingNumber4(self, nums: List[int]) -> int:
        '''
        执行用时 :56 ms, 在所有 Python3 提交中击败了77.10%的用户
        内存消耗 :14.5 MB, 在所有 Python3 提交中击败了11.71%的用户
        思路：^异或
        :param nums:
        :return:
        '''
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res