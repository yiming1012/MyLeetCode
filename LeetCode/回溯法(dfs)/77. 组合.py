"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        思路：回溯法
        1. 存在顺序，所以记录下一次遍历的位置即可
        @param n:
        @param k:
        @return:
        """
        def backtrack(cur, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return

            for i in range(cur, n + 1):
                backtrack(i + 1, arr + [i])

        res = []
        backtrack(1, [])
        return res


if __name__ == '__main__':
    n, k = 4, 2
    print(Solution().combine(n, k))
