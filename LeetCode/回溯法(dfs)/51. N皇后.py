"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例：

输入：4
输出：[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
 

提示：

皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        思路：回溯法
        1. 从上到下放皇后
        2. 每个点需要判断三个方向上是否放了皇后：左上方、正上方和右上方
        3. 关键点：
            1）左上方所有位置(i,j)的横纵坐标之差（i-j）相等
            2）右上方所有位置(i,j)的横纵坐标之和（i+j）相等
            3）正上方所有位置(i,j)的纵坐标j相等
        @param n:
        @return:
        """
        # v、vl、vr分别表示正上方、左上方、右上方的集合
        v = set()
        vl = set()
        vr = set()
        res = []

        def backtrack(cur, arr):
            if cur == n:
                res.append(arr.copy())
                return

            s = ["."] * n
            for j in range(n):
                if j not in v and cur - j not in vl and cur + j not in vr:
                    v.add(j)
                    vl.add(cur - j)
                    vr.add(cur + j)
                    s[j] = "Q"
                    backtrack(cur + 1, arr + ["".join(s)])
                    s[j] = "."
                    v.remove(j)
                    vl.remove(cur - j)
                    vr.remove(cur + j)

        backtrack(0, [])
        return res


if __name__ == '__main__':
    n = 8
    print(Solution().solveNQueens(n))
