"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import bisect
from typing import List


class Solution:
    def minSubArrayLen1(self, s: int, nums: List[int]) -> int:
        """
        思路：滑动窗口
        1. 题目中如果是求等于s的最小子数组，解法是前缀和+哈希
        2. 本题要求大于等于s的最短连续子数组，可用滑动窗口实现
        """
        preSum = 0
        res = float('inf')
        start = 0
        for i, num in enumerate(nums):
            preSum += num
            # 滑动窗口标志：while循环
            while preSum >= s:
                res = min(res, i - start + 1)
                preSum -= nums[start]
                start += 1
        return 0 if res == float('inf') else res

    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])
        print(sums)

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            # 利用二分查找找到当前位置到前面
            bound = bisect.bisect_left(sums, target)
            print("bound:",target, bound)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen1(s, nums))
    print(Solution().minSubArrayLen2(s, nums))
