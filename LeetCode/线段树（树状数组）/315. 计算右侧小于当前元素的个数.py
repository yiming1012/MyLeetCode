"""
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0]
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class BinaryIndexedTree:
    def __init__(self, length):
        self.c = [0] * length

    def lowBit(self, x):
        return x & (-x)

    def update(self, pos, value=1):
        while pos < len(self.c):
            self.c[pos] += value
            pos += self.lowBit(pos)

    def query(self, pos):
        ans = 0
        while pos > 0:
            ans += self.c[pos]
            pos -= self.lowBit(pos)
        return ans


class Solution:
    def discretization(self, nums):
        a = sorted(set(nums))
        value2ID = {v: i + 1 for i, v in enumerate(a)}
        return value2ID, len(a)

    def countSmaller(self, nums: List[int]) -> List[int]:
        value2ID, length = self.discretization(nums)
        BIT = BinaryIndexedTree(length + 1)
        ans = []

        for i in reversed(range(len(nums))):
            posID = value2ID[nums[i]]
            ans.append(BIT.query(posID - 1))
            BIT.update(posID)

        return ans[::-1]