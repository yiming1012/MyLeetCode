"""
254. 因子的组合
整数可以被看作是其因子的乘积。

例如：

8 = 2 x 2 x 2;
  = 2 x 4.
请实现一个函数，该函数接收一个整数 n 并返回该整数所有的因子组合。

注意：

你可以假定 n 为永远为正数。
因子必须大于 1 并且小于 n。
示例 1：

输入: 1
输出: []
示例 2：

输入: 37
输出: []
示例 3：

输入: 12
输出:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
示例 4:

输入: 32
输出:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factor-combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        """
        思路：回溯法
        @param n:
        @return:
        """
        res = []

        def helper(n, i, tmp):
            if n == 1:
                if len(tmp) > 1:
                    res.append(tmp)
                return
            for j in range(i, n + 1):
                if n % j == 0:
                    helper(n // j, j, tmp + [j])

        helper(n, 2, [])
        return res


if __name__ == '__main__':
    n = 12
    print(Solution().getFactors(n))
