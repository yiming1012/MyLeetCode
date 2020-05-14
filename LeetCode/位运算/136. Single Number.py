'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        执行用时 :32 ms, 在所有 Python3 提交中击败了98.93%的用户
        内存消耗 :15.2 MB, 在所有 Python3 提交中击败了15.80%的用户
        思路：
        a ^ a = 0
        a ^ 0 = 0
        :param nums:
        :return:
        '''
        res = 0
        for num in nums:
            res ^= num
        return res

    def singleNumber2(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)

    def singleNumber3(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    print(Solution().singleNumber3([2, 2, 3, 3, 1]))
