'''
Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def sortArray1(self, nums: List[int]) -> List[int]:
        '''
        执行用时 :300 ms, 在所有 Python3 提交中击败了59.20%的用户
        内存消耗 :20 MB, 在所有 Python3 提交中击败了5.71%的用户
        思路：快速排序
        时间复杂度：O(nlogn)
        空间复杂度：O(1)
        :param nums:
        :return:
        '''

        def quickSort(x, y):
            left, right = x, y
            pivot = nums[right]
            if left < right:
                while left < right:
                    while left < right and nums[left] <= pivot:
                        left += 1
                    while left < right and nums[right] >= pivot:
                        right -= 1
                    nums[left], nums[right] = nums[right], nums[left]
                nums[left], nums[y] = nums[y], nums[left]
                # print(pivot,nums)
                quickSort(x, left - 1)
                quickSort(left + 1, y)

        # return sorted(nums)
        left, right = 0, len(nums) - 1
        quickSort(left, right)
        return nums

    def sortArray2(self, nums: List[int]) -> List[int]:
        '''
        执行用时 :480 ms, 在所有 Python3 提交中击败了24.65%的用户
        内存消耗 :20.7 MB, 在所有 Python3 提交中击败了5.71%的用户
        快速排序：三部分
        :param nums:
        :return:
        '''

        def quickSort(nums):
            if len(nums) < 2:
                return nums
            pivot = nums[0]
            left, right = [], []
            for i in nums[1:]:
                if i <= pivot:
                    left.append(i)
                else:
                    right.append(i)

            return quickSort(left) + [pivot] + quickSort(right)

        return quickSort(nums)

    def sortArray3(self, nums: List[int]) -> List[int]:
        '''
        选择排序：nums[i]与nums[j]比较，nums[i]更大就交换
        :param nums:
        :return:
        '''
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums

    def sortArray4(self, nums: List[int]) -> List[int]:
        '''
        思路：归并排序
        :param nums:
        :return:
        '''

        def helper(nums):
            if len(nums) < 2:
                return nums
            key = nums[0]
            left = [i for i in nums[1:] if i <= key]
            right = [i for i in nums[1:] if i > key]
            return helper(left) + [key] + helper(right)

        return helper(nums)

    def sortArray5(self, nums: List[int]) -> List[int]:
        """
        思路：冒泡排序
        1. 将相邻的两个数中较大的数移到最上面，就像冒泡一样
        2. 优化：如果某一遍历，数组中的元素没有交换位置，说明已经有序，可退出
        :param nums:
        :return:
        """
        for i in range(len(nums) - 1, -1, -1):
            flag = 0
            for j in range(1, i + 1):
                if nums[j - 1] > nums[j]:
                    flag = 1
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
            if flag == 0:
                break
        return nums


if __name__ == '__main__':
    nums = [5, 3, 4, 1, 2]
    s = Solution()
    print(s.sortArray1(nums))
    print(s.sortArray2(nums))
    print(s.sortArray3(nums))
    print(s.sortArray4(nums))
    print(s.sortArray5(nums))
