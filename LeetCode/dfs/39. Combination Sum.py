'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        思路：1.
        :param candidates:
        :param target:
        :return:
        '''

        def dfs(arr, index):
            if sum(arr) == target:
                res.append(arr)
                return

            for i, num in enumerate(candidates):
                if i >= index and sum(arr) + num <= target:
                    dfs(arr + [num], i)

        res = []
        dfs([], 0)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了89.99%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.00%的用户
        :param candidates:
        :param target:
        :return:
        '''
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp):
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j, tmp_sum + candidates[j], tmp + [candidates[j]])

        backtrack(0, 0, [])
        return res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum2(candidates, target))
