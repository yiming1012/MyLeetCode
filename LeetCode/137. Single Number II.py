'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        思路：hashmap
        :param nums:
        :return:
        '''
        dic=collections.Counter(nums)
        for key in dic:
            # print(key,dic[key])
            if dic[key]==1:
                return key

    def singleNumber2(self, nums: List[int]) -> int:
        '''
        思路：位运算
        :param nums:
        :return:
        '''
        res = 0
        for i in range(32):
            sum = 0
            for num in nums:
                sum += (num >> i) & 1
            res |= (sum % 3) << i

        return res if res <= 0x7FFFFFFF else ~(res ^ 0xFFFFFFFF)

    def singleNumber3(self, nums):
        '''
        思路：先将不同数求出来*3，减掉原来的数据，就只剩2*singleNumber
        :param self:
        :param nums:
        :return:
        '''
        return (3 * sum(set(nums)) - sum(nums)) / 2


    def singleNumber(self, nums: [int]) -> int:
        '''
        思路：模拟三进制 00-10-01-00
        :param nums:
        :return:
        '''
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones

