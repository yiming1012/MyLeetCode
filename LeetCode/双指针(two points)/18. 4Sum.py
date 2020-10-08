'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        思路：双指针
        1. 排序+两层for循环+双指针，时间复杂度O(N**3)
        2. 优化：
            · 如果最小数之和大于target，break退出；
            · 如果最大数之和小于target，continue继续向后遍历
        3. 去重：
            · 第一层遍历中，如果某个位置的值与前一个相等，即i > 0 and nums[i] == nums[i - 1]，则跳过
            · 第二层遍历中，如果某个位置的值与前一个相等，即j > i + 1 and nums[j] == nums[j - 1]，则跳过
            · 第三层双指针的遍历：
                1. 如果四数之和小于target，左边的指针向右移动，使得新增的数增大，从而满足条件
                2. 如果四数之和大于target，右边的指针向左移动，使得新增的数减小，从而满足条件
                3. 如果四数之和等于target，将四个数添加到结果集，同时将左指针右移，右指针左移。
                    注：这里可能出现左指针右边的元素和当前元素相等以及右指针左边的元素和当前元素相等，所以需要用到while循环判断，直到遇到不同的值为止
        @param nums:
        @param target:
        @return:
        """
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] * 4 > target:
                break
            if nums[n - 1] * 4 < target:
                break
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, n - 1
                if nums[i] + nums[j] + 2 * nums[r] < target:
                    continue
                if nums[i] + nums[j] + 2 * nums[l] > target:
                    break

                while l < r:
                    num = nums[i] + nums[j] + nums[l] + nums[r]
                    if num == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif num > target:
                        r -= 1
                    else:
                        l += 1
        return res


if __name__ == '__main__':
    arr = [-1, 0, 1, 2, -1, -4]
    target = 0
    print(Solution().fourSum(arr, target))
