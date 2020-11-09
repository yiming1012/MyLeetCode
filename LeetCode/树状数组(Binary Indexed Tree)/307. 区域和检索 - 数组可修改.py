"""
307. 区域和检索 - 数组可修改
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。

示例:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
说明:

数组仅可以在 update 函数下进行修改。
你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-mutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class NumArray:
    def lowbit(self, x):
        return x & (-x)

    def query(self, x):
        res = 0
        while x:
            res += self.treeval[x]
            x -= self.lowbit(x)
        return res

    def add(self, x, val):
        while x < self.n + 1:
            self.treeval[x] += val
            x += self.lowbit(x)

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        # 定义树状数组
        self.treeval = [0] * (self.n + 1)
        for i, num in enumerate(nums):
            self.add(i + 1, num)

    def update(self, i: int, val: int) -> None:
        self.add(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.query(j + 1) - self.query(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
