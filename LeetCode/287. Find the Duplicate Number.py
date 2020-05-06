'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
通过次数44,731提交次数70,288

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        执行用时 :80 ms, 在所有 Python3 提交中击败了73.38%的用户
        内存消耗 :16 MB, 在所有 Python3 提交中击败了16.66%的用户
        思路：利用快慢指针实现
        :param nums:
        :return:
        '''
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        first = 0
        while True:
            slow = nums[slow]
            first = nums[first]
            if slow == first:
                return slow


    def findDuplicate(self, nums: List[int]) -> int:
        '''
        如果可以改变nums的话
        :param nums:
        :return:
        '''
        pre = 0
        while nums[0] != pre:
            pre = nums[0]
            nums[0] = nums[pre]
            nums[pre] = pre
        return nums[0]


