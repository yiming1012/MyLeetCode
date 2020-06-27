"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        """
        思路：
        1. 第一遍for循环，把下标和数值一一对应
        2. 第二遍for循环，判断下标和数值不对应的
        """
        res = []
        for i, num in enumerate(nums):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i, num in enumerate(nums):
            if num != i + 1:
                res.append(i + 1)
        return res

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        """
        思路：将存在下标对应的数变为相反数，最后只需找出为正数对应的下标即可
        """
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res

    def findDisappearedNumbers3(self, nums: List[int]) -> List[int]:
        """
        思路：利用set的差集
        """
        return set(list(range(1, len(nums) + 1))) - set(nums)


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers1(nums))
    # print(Solution().findDisappearedNumbers2(nums))
    # print(Solution().findDisappearedNumbers3(nums))
