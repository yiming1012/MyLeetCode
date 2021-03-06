"""
5691. 通过最少操作次数使数组的和相等
给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。

每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。

请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。



示例 1：

输入：nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums2[0] 变为 6 。 nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[5] 变为 1 。 nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[2] 变为 2 。 nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2] 。
示例 2：

输入：nums1 = [1,1,1,1,1,1,1], nums2 = [6]
输出：-1
解释：没有办法减少 nums1 的和或者增加 nums2 的和使二者相等。
示例 3：

输入：nums1 = [6,6], nums2 = [1]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums1[0] 变为 2 。 nums1 = [2,6], nums2 = [1] 。
- 将 nums1[1] 变为 2 。 nums1 = [2,2], nums2 = [1] 。
- 将 nums2[0] 变为 4 。 nums1 = [2,2], nums2 = [4] 。


提示：

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6
"""
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = sum(nums1), sum(nums2)
        if a == b:
            return 0
        if a > b:
            nums1, nums2 = nums2, nums1
            a, b = b, a

        diff = b - a
        max1 = len(nums1) * 6
        min2 = len(nums2)
        if max1 < min2:
            return -1

        arr1 = [6 - num for num in nums1]
        arr2 = [num - 1 for num in nums2]
        arr = arr1 + arr2
        arr.sort(reverse=True)
        for i, a in enumerate(arr):
            diff -= a
            if diff <= 0:
                return i + 1
        if diff > 0:
            return -1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [1, 1, 2, 2, 2, 2]
    print(Solution().minOperations(nums1, nums2))
