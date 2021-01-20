"""
628. 三个数的最大乘积
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maximumProduct1(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]
        return max(a, b)

    def maximumProduct2(self, nums: List[int]) -> int:
        a = b = c = float('-inf')
        d = e = float('inf')
        for i, num in enumerate(nums):
            if num > a:
                a, b, c = num, a, b
            elif num > b:
                b, c = num, b
            elif num > c:
                c = num

            if num < d:
                d, e = num, d
            elif num < e:
                e = num

        return max(d * e * a, a * b * c)


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().maximumProduct1(nums))
    print(Solution().maximumProduct2(nums))
