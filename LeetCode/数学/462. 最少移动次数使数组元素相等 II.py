"""
462. 最少移动次数使数组元素相等 II
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

例如:

输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）：

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # |num1-x|+|num2-x|+|num3-x|+……+|numK-x|=S
        nums.sort()
        n = len(nums)
        mid = nums[n // 2]
        res = 0
        for num in nums:
            res += abs(mid - num)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().minMoves2(nums))
