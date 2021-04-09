"""
259. 较小的三数之和
给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。

示例：

输入: nums = [-2,0,1,3], target = 2
输出: 2
解释: 因为一共有两个三元组满足累加和小于 2:
     [-2,0,1]
     [-2,0,3]
进阶：是否能在 O(n2) 的时间复杂度内解决？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-smaller
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n - 2):
            l, r = i + 1, n - 1
            if nums[i] + nums[l] + nums[l] >= target: break
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t >= target:
                    r -= 1
                else:
                    res += r - l
                    l += 1
        return res


if __name__ == '__main__':
    nums = [-2, 0, 1, 3]
    target = 2
    print(Solution().threeSumSmaller(nums, target))
