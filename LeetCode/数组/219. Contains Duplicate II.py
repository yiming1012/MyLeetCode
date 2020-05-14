'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        执行用时 :48 ms, 在所有 Python3 提交中击败了87.54%的用户
        内存消耗 :21.2 MB, 在所有 Python3 提交中击败了10.39%的用户
        :param nums:
        :param k:
        :return:
        '''
        if len(nums) == 0:
            return False
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic and i - dic[nums[i]] <= k:
                return True
            dic[nums[i]] = i
        return False
