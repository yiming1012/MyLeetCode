'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        执行用时 :68 ms, 在所有 Python3 提交中击败了82.60%的用户
        内存消耗 :15.2 MB, 在所有 Python3 提交中击败了5.04%的用户
        :param nums:
        :return:
        '''
        half = (len(nums) + 1) // 2
        dict = {}
        for j in nums:
            dict[j] = dict[j] + 1 if j in dict else 1
            if dict[j] >= half:
                return j

    def majorityElement2(self, nums: List[int]) -> int:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了95.42%的用户
        内存消耗 :15.2 MB, 在所有 Python3 提交中击败了5.04%的用户
        摩尔投票算法：如果和当前的第一个相同，+1，否则-1.遇到等于0时，将开头元素指向下一个
        :param nums:
        :return:
        '''
        num = nums[0]
        count = 0
        for j in range(len(nums)):
            if num == nums[j]:
                count += 1
            else:
                count -= 1
                if count == 0 and j + 1 < len(nums):
                    num = nums[j + 1]
        return num

    def majorityElement2(self, nums: List[int]) -> int:
        '''
        执行用时 :60 ms, 在所有 Python3 提交中击败了85.01%的用户
        内存消耗 :15 MB, 在所有 Python3 提交中击败了5.04%的用户
        Solution:如果一定存在超过半数的数，排序后中位数就是
        :param nums:
        :return:
        '''
        nums.sort()
        return nums[len(nums) // 2]