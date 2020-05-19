'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了94.23%的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了11.11%的用户
        :param nums:
        :return:
        '''
        if len(nums) == 0:
            return 0
        result = nums[0]
        tmp = 1
        for num in nums:
            tmp *= num
            result = max(result, tmp)
            if num == 0:
                tmp = 1

        tmp = 1
        for num in nums[::-1]:
            tmp *= num
            result = max(result, tmp)
            if num == 0:
                tmp = 1

        return result

    def maxProduct2(self, nums: List[int]) -> int:
        '''
        思路：此题是对上面的化简
        在python里 -1 or 1 = -1; 1 or 1 = 1; 0 or 1 = 1
        如果前一项的结果为0，此时的结果就是nums[i]*1
        :param nums:
        :return:
        '''
        reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse[i] *= reverse[i - 1] or 1
        return max(max(nums), max(reverse))

    def maxProduct3(self, nums: List[int]) -> int:
        """
        执行用时 :48 ms, 在所有 Python3 提交中击败了83.87%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了12.50%的用户
        思路：
        1. 因为是子数组的乘积，存在负负得正的情况，所以每一步都要记录当前的最大值和最小值
        2. 当遇到负数时，需要交换前面保存的最大值最小值，再和当前负数计算，才能得到正确的最大值和最小值
        """
        res = nums[0]
        a, b = 1, 1
        for num in nums:
            if num < 0:
                a, b = b, a
            a = max(a * num, num)
            b = min(b * num, num)
            res = max(a, res)
        return res


if __name__ == '__main__':
    arr = [2, 3, -2, 4, 6]
    arr1 = [9, 3, -2, 4, 6]
    print(Solution().maxProduct3(arr1))
