'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        思路：回溯+去重
        1. 去重的关键在于，可以让同一层级，不出现相同的元素。但是却允许了不同层级之间的重复

                          1
                         / \
                        2   2  这种情况不会发生
                       /     \
                      5       5
                        例2
                          1
                         /
                        2      这种情况确是允许的
                       /
                      2
        为何会有这种神奇的效果呢？
        首先 cur-1 == cur 是用于判定当前元素是否和之前元素相同的语句。这个语句就能砍掉例1。可是问题来了，如果把所有当前与之前一个元素相同的都砍掉，那么例二的情况也会消失。 因为当第二个2出现的时候，他就和前一个2相同了

        那么如何保留例2呢？
        那么就用cur > begin 来避免这种情况，你发现例1中的两个2是处在同一个层级上的，
        例2的两个2是处在不同层级上的。在一个for循环中，所有被遍历到的数都是属于一个层级的。我们要让一个层级中，必须出现且只出现一个2，那么就放过第一个出现重复的2，但不放过后面出现的2。第一个出现的2的特点就是 cur == begin. 第二个出现的2 特点是cur > begin.

        @param candidates:
        @param target:
        @return:
        """
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(index, presum, arr):
            if presum == target:
                res.append(arr.copy())
                return
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] + presum <= target:
                    backtrack(i + 1, presum + candidates[i], arr + [candidates[i]])
                else:
                    break

        backtrack(0, 0, [])
        return res


if __name__ == '__main__':
    candidates = [1, 2, 2, 2, 3, 3, 6, 7, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
