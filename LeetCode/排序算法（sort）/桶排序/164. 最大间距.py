"""
164. 最大间距
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-gap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0

        n = len(nums)
        max_ = max(nums)
        min_ = min(nums)
        bucket_len = max(1, (max_ - min_) // (n - 1))
        bucket_num = (max_ - min_) // bucket_len + 1
        bucket = [[] * bucket_len for _ in range(bucket_num)]
        for num in nums:
            index = (num - min_) // bucket_len
            bucket[index].append(num)
        print(bucket)

        pre = float('inf')
        res = 0
        for arr in bucket:
            if arr:
                maxarr_ = max(arr)
                minarr_ = min(arr)

                if pre != float('inf'):
                    res = max(res, minarr_ - pre)
                pre = maxarr_

        return res


if __name__ == '__main__':
    nums = [1, 10000000]
    print(Solution().maximumGap(nums))
