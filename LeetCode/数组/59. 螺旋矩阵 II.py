"""
59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 

示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
 

提示：

1 <= n <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        x, y = 0, -1
        matrix = [[0] * n for _ in range(n)]
        for i in range(n * n):
            xx, yy = x + pos[d][0], y + pos[d][1]
            if not (0 <= xx < n and 0 <= yy < n) or matrix[xx][yy]:
                d = (d + 1) % 4
                xx, yy = x + pos[d][0], y + pos[d][1]
            matrix[xx][yy] = i + 1
            x, y = xx, yy
        return matrix


if __name__ == '__main__':
    n = 3
    print(Solution().generateMatrix(n))
