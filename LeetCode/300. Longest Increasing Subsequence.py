'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        执行用时 :1540 ms, 在所有 Python3 提交中击败了21.08%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.11%的用户
        :param nums:
        :return:
        '''
        if len(nums) == 0:
            return 0
        arr = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    arr[i] = max(arr[i], arr[j] + 1)

        return max(arr)
