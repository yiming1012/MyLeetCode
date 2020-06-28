'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        执行用时 :32 ms, 在所有 Python3 提交中击败了96.03%的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.36%的用户
        思路：遍历寻找转折点，时间复杂度：O(n)
        :param nums:
        :return:
        '''
        fisrt = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return fisrt

    def findMin2(self, nums: List[int]) -> int:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了48.07%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.36%的用户
        思路：如果首项和尾项相同，则尾项-1向前移动一位
        :param nums:
        :return:
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            if nums[left] == nums[right]:
                right -= 1
                continue
            # risk of overflow: pivot = (low + high) // 2
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    def findMin3(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while high > low:
            pivot = low + (high - low) // 2
            # risk of overflow: pivot = (low + high) // 2
            # Case 1):
            if nums[pivot] < nums[high]:
                high = pivot
                # alternative: high = pivot - 1
                # too aggressive to move the `high` index,
                # it won't work for the test case of [3, 1, 3]
            # Case 2):
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            # Case 3):
            else:
                high -= 1
        # the 'low' and 'high' index converge to the inflection point.
        return nums[low]

