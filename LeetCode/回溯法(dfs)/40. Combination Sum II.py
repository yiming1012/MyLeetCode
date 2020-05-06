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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(arr, visited):
            if sum(arr) == target:
                tmp = sorted(arr)
                if tmp not in res:
                    res.append(tmp)
                return
            if sum(arr) > target:
                return

            for i, num in enumerate(candidates):
                if i not in visited and i > visited[0]:
                    visited.append(i)
                    arr.append(num)
                    dfs(arr, visited)
                    arr.pop()
                    visited.pop()

        res = list(set())
        dfs([], [])
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()

        def dfs(arr, index):
            if sum(arr) == target:
                if arr not in res:
                    res.append(arr)
                return

            for i in range(index, n):
                if sum(arr) + candidates[i] > target:
                    break
                dfs(arr + [candidates[i]], i + 1)

        res = list(set())
        dfs([], 0)
        return res

    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()

        def dfs(arr, index):
            if sum(arr) == target:
                res.append(arr)
                return

            for i in range(index, n):
                # if len(arr)==0 and i>0 and candidates[i]==candidates[i-1]:
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if sum(arr) + candidates[i] > target:
                    break
                dfs(arr + [candidates[i]], i + 1)

        res = list(set())
        dfs([], 0)
        return res

'''
这个避免重复当思想是在是太重要了。
这个方法最重要的作用是，可以让同一层级，不出现相同的元素。但是却允许了不同层级之间的重复

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
首先 cur-1 == cur 是用于判定当前元素是否和之前元素相同的语句。这个语句就能砍掉例1。可是问题来了，如果把所有当前与之前一个元素相同的都砍掉，那么例二的情况也会消失。 因为当第二个2出现的时候，他就和前一个2相同了。

那么如何保留例2呢？
那么就用cur > begin 来避免这种情况，你发现例1中的两个2是处在同一个层级上的，
例2的两个2是处在不同层级上的。在一个for循环中，所有被遍历到的数都是属于一个层级的。我们要让一个层级中，必须出现且只出现一个2，那么就放过第一个出现重复的2，但不放过后面出现的2。第一个出现的2的特点就是 cur == begin. 第二个出现的2 特点是cur > begin.

作者：allen-238
链接：https://leetcode-cn.com/problems/combination-sum-ii/solution/xiang-xi-jiang-jie-ru-he-bi-mian-zhong-fu-by-allen/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    candidates = [2, 2, 2, 3, 3, 6, 7, 7]
    target = 7
    print(Solution().combinationSum3(candidates, target))
