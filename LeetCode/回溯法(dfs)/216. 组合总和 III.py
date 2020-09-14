"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import itertools
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        思路：回溯+剪枝
        1. 往res结果集中添加当前满足条件的组合列表时，需要用到浅拷贝
        2. 当target为组合之和时，可以考虑用“-”来操作，直到为0判断是否满足条件
        @param k:
        @param n:
        @return:
        """

        def dfs(index=1, target=n, arr=[]):
            if target == 0 and len(arr) == k:
                res.append(arr.copy())
                return

            for i in range(index, 10):
                dfs(i + 1, target - i, arr + [i])

        res = []
        dfs()
        return res

    def combinationSum31(self, k: int, n: int) -> List[List[int]]:
        return list(filter(lambda l: sum(l) == n, itertools.combinations(range(1, 10), k)))


if __name__ == '__main__':
    k, n = 3, 7
    print(Solution().combinationSum3(k, n))
    print(Solution().combinationSum31(k, n))
