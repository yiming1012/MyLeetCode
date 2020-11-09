"""
给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

说明:
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例:

输入: nums = [-2,5,-1], lower = -2, upper = 2,
输出: 3
解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-range-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, num in enumerate(nums):
            pre[i + 1] = pre[i] + nums[i]
        res = 0

        def sort(arr):
            if len(arr) < 2:
                return arr
            mid = len(arr) // 2
            left = sort(arr[:mid])
            right = sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            m, n = len(left), len(right)
            # 统计满足条件的个数
            i, j = 0, 0
            for L in left:
                while i < n and right[i] - L < lower: i += 1
                while j < n and right[j] - L <= upper: j += 1
                nonlocal res
                res += j - i

            i, j = 0, 0
            arr = []
            while i < m and j < n:
                if left[i] <= right[j]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1
            if i < m:
                arr.extend(left[i:])
            if j < n:
                arr.extend(right[j:])
            return arr

        sort(pre)
        return res


if __name__ == '__main__':
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    print(Solution().countRangeSum(nums, lower, upper))
