'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了78.02%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了7.69%的用户
        思路：分别计算有一个数和没有第一个数的情况，取最大值
        :param nums:
        :return:
        '''
        if len(nums) == 1:
            return nums[0]

        a, b = 0, 0
        for i in range(len(nums) - 1):
            b, a = max(a + nums[i], b), b
        # print(b)
        b1 = b

        a, b = 0, 0
        for i in range(1, len(nums)):
            b, a = max(a + nums[i], b), b
        # print(b)

        return max(b, b1)
