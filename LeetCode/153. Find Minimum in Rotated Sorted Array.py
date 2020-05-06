'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        执行用时 :32 ms, 在所有 Python3 提交中击败了95.68%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.26%的用户
        思路：二分查找法。因为没有重复元素且单调递增，所以只要是nums[left]<=nums[mid],left=mid+1,反之，right=mid
        :param nums:
        :return:
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    def findMin2(self, nums: List[int]) -> int:
        '''
        min太秀了
        :param nums:
        :return:
        '''
        return min(nums)

    def findMin3(self, nums: List[int]) -> int:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了88.01%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.26%的用户
        标准解法
        :param nums:
        :return:
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            # 如果 mid = (left + right) // 2 可能会溢出
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    s = Solution()
    print(s.findMin2(nums))
