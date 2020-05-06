'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        执行用时 :2180 ms, 在所有 Python3 提交中击败了5.03%的用户
        内存消耗 :14 MB, 在所有 Python3 提交中击败了5.78%的用户
        :param nums:
        :return:
        '''
        def backtrack(sol, check):
            if len(sol) == len(nums) and sol not in res:
                res.append(sol)
                return

            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                check[i] = 1
                backtrack(sol + [nums[i]], check)
                check[i] = 0

        res = []
        check = [0 for i in range(len(nums))]
        backtrack([], check)
        return res