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
        """
        思路：关键在于去重
        1. 如果当前数字和前一个相同，并且前一个没有被访问过，那说明前一个数字被回溯过，此时需要跳过避免重复计算
        2. 以[1,1,2]为例，当第二个1出现时，看看前面一个1是否被访问过，如果不在同一层，则说明前面的已经被访问过了，所以这一轮continue
        3. if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:continue
        @param nums:
        @return:
        """
        nums.sort()
        print(nums)
        n = len(nums)
        res = []
        visited = [False] * n

        def backtrack(arr):
            print(arr)
            if len(arr) == n:
                res.append(arr.copy())
                return
            for i, num in enumerate(nums):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                if not visited[i]:
                    visited[i] = True
                    backtrack(arr + [num])
                    visited[i] = False

        backtrack([])
        return res


if __name__ == '__main__':
    nums = [2, 3, 3, 4]
    print(Solution().permuteUnique(nums))
