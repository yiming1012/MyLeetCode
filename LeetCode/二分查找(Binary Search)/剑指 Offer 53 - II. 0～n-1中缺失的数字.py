"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 

限制：

1 <= 数组长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        """
        思路：顺序遍历，当前数和下标不相等，则输出i
        """
        for i, num in enumerate(nums):
            if num != i:
                return i
        return len(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        """
        思路：二分法
        1. 巧妙利用数组有序的特性，使用二分查找
        2. 如果mid==i,说明res在右边，反之，res在左边
        """
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > mid:
                right = mid
            else:
                left += 1
        return left

    def missingNumber3(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if mid == nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return i


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    print(Solution().missingNumber1(nums))
    print(Solution().missingNumber2(nums))
    print(Solution().missingNumber3(nums))
