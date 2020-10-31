"""
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def dfs(start, arr):
            if len(arr) > 1:
                res.append(arr.copy())
            if start == len(nums):
                return

            memo = set()

            for i in range(start, len(nums)):
                if nums[i] not in memo and (not arr or arr[-1] <= nums[i]):
                    memo.add(nums[i])
                    dfs(i + 1, arr + [nums[i]])

        res = []
        dfs(0, [])
        return res


if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    print(Solution().findSubsequences(nums))
