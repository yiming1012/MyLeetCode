"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes1(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] == 0:
                res = max(res, count)
                count = 0
            else:
                count += 1

        return max(res, count)

    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        return max(list(map(len, ''.join(map(str, nums)).split("0"))))


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    print(Solution().findMaxConsecutiveOnes1(nums))
    print(Solution().findMaxConsecutiveOnes2(nums))
