'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums)
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[left] == 0:
                right += 1
                if right < n and nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
            else:
                left += 1

        print(nums)
        return nums


    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums)
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] != 0:
                left += 1
            right += 1

        print(nums)
        return nums


    def moveZeroes3(self, nums: List[int]) -> None:
        '''
        执行用时 :48 ms, 在所有 Python3 提交中击败了71.39%的用户
        内存消耗 :14.3 MB, 在所有 Python3 提交中击败了5.58%的用户
        思路：j总是指向
        :param nums:
        :return:
        '''
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                

    def moveZeroes4(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif count > 0:
                nums[i - count] = nums[i]
                nums[i] = 0

    def moveZeroes5(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index, value in enumerate(nums):
                    if value == 0:
                        nums.remove(value)
                        nums.append(0)


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    s = Solution()
    print(s.moveZeroes2(nums))
