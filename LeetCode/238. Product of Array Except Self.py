'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/product-of-array-except-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        执行用时 :72 ms, 在所有 Python3 提交中击败了69.30%的用户
        内存消耗 :19.5 MB, 在所有 Python3 提交中击败了35.51%的用户
        思路：
        1、获取每个位置左边和右边的乘积，存在两个list中即可
        2、遍历将每个位置的左右乘积相乘即可
        :param nums:
        :return:
        '''
        n = len(nums)
        left = [1] * n
        right = [1] * n
        res = []

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            res.append(left[i] * right[i])
        return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了94.08%的用户
        内存消耗 :17.8 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param nums:
        :return:
        '''
        n = len(nums)
        left = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        mul = 1
        for i in range(n - 1, -1, -1):
            left[i] *= mul
            mul *= nums[i]

        return left

    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        '''
        执行用时 :92 ms, 在所有 Python3 提交中击败了59.31%的用户
        内存消耗 :17.7 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param nums:
        :return:
        '''
        n = len(nums)
        flagA, flagB = 1, 1
        res = [1] * n
        for i in range(n):
            res[i] *= flagA
            flagA *= nums[i]

            res[n - i - 1] *= flagB
            flagB *= nums[n - i - 1]

        return res