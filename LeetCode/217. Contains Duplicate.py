'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了98.06%的用户
        内存消耗 :21.8 MB, 在所有 Python3 提交中击败了5.05%的用户
        :param nums:
        :return:
        '''
        if len(nums) <= 1:
            return False
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            dic[nums[i]] = i

        return False