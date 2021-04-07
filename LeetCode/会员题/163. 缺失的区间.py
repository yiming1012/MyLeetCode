"""
163. 缺失的区间
给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。

示例：

输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
输出: ["2", "4->49", "51->74", "76->99"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        low = lower - 1
        nums.append(upper + 1)
        res = []
        for num in nums:
            diff = num - low
            if diff == 2:
                res.append(str(low + 1))
            elif diff > 2:
                res.append(str(low + 1) + "->" + str(num - 1))
            low = num
        return res
