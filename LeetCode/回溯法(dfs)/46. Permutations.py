'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import itertools
from typing import List
import inspect


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了80.15%的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.16%的用户
        注意事项：res.append(arr)后，如果arr的值更改了，res里面的值也会跟着一起改变
        所以使用copy浅拷贝来赋值
        :param nums:
        :return:
        '''

        def dfs(arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            for num in nums:
                if num not in arr:
                    arr.append(num)
                    dfs(arr)
                    a = arr.pop()
                    print(a)

        res = []

        dfs([])
        print(res)
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        '''
        执行用时 :64 ms, 在所有 Python3 提交中击败了14.92%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.16%的用户
        内置函数：itertools
        :param nums:
        :return:
        '''
        return list(itertools.permutations(nums))

    def permute3(self, nums: List[int]) -> List[List[int]]:
        '''
        执行用时 :48 ms, 在所有 Python3 提交中击败了41.80%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.16%的用户
        思路：通过check来标记元素是否被访问过
        :param nums:
        :return:
        '''

        # 回溯法
        def backtrack(sol, check):
            if len(sol) == len(nums):
                print("sol:", sol)
                res.append(sol)
                return

            for i in range(len(nums)):
                print("i:", i)
                if check[i] == 1:
                    continue
                check[i] = 1
                print("before:", check)
                backtrack(sol + [nums[i]], check)
                check[i] = 0
                print("after:", check, sol)

        res = []
        check = [0 for i in range(len(nums))]
        backtrack([], check)
        return res

    def permute4(self, nums: List[int]) -> List[List[int]]:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了80.15%的用户
        内存消耗 :14 MB, 在所有 Python3 提交中击败了5.16%的用户
        思路：将check标记去掉
        :param nums:
        :return:
        '''

        def backtrack(sol):
            if len(sol) == length:
                res.append(sol)
                return

            for i in range(len(nums)):
                if nums[i] not in sol:
                    backtrack(sol + [nums[i]])

        res = []
        length = len(nums)
        backtrack([])
        return res

    def permute5(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, tmp):
            if not nums:
                print(tmp)
                res.append(tmp)
                return
            for i in range(len(nums)):
                print(i, nums[:i], nums[i + 1:])
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.permute(nums))
