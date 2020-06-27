"""
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

 

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
 

提示：

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(-1)
        n = len(nums)
        for i, num in enumerate(nums):
            # 先判断下标对应的数字是否在索引范围内 and 对应的位置的数字是否正确，关键是nums[i]!=nums[nums[i]-1]
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                # 下面如果写成nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]会报错
                # 写成nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] 是正确的
                nums[i], nums[j] = nums[j], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        else:
            return n


if __name__ == '__main__':
    nums = [1, 2, -1]
    print(Solution().firstMissingPositive(nums))
