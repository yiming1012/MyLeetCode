"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.presum = [0]
        for num in nums:
            self.presum.append(self.presum[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.presum[min(self.n, j + 1)] - self.presum[max(i, 0)]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)