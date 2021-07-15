"""
面试题 17.19. 消失的两个数字
给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

以任意顺序返回这两个数字均可。

示例 1:

输入: [1]
输出: [2,3]
示例 2:

输入: [2,3]
输出: [1,4]
提示：

nums.length <= 30000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-two-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = n + 2
        a = reduce(xor, range(1, m + 1))
        b = reduce(xor, nums)
        c = a ^ b
        x = c & (-c)
        r1, r2 = 0, 0
        for num in nums:
            if num & x == x:
                r1 ^= num
            else:
                r2 ^= num

        for i in range(1, m + 1):
            if i & x == x:
                r1 ^= i
            else:
                r2 ^= i

        return [r1, r2]


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        m = len(nums) + 2
        add = lambda x, y: x + y
        mul = lambda x, y: x * y
        x = reduce(add, range(1, m + 1)) - reduce(add, nums)
        y = reduce(mul, range(1, m + 1)) // reduce(mul, nums)
        a = int(x + (x * x - 4 * y) ** 0.5) // 2
        return [a, x - a]
