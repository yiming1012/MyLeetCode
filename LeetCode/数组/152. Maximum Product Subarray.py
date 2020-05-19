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
        if not nums:
            return
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res


if __name__ == '__main__':
    arr = [2, 3, -2, 4, 6]
    print(Solution().maxProduct2(arr))
