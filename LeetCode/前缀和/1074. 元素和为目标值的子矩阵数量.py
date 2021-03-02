"""
1074. 元素和为目标值的子矩阵数量
给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。

子矩阵 x1, y1, x2, y2 是满足 x1 <= x <= x2 且 y1 <= y <= y2 的所有单元 matrix[x][y] 的集合。

如果 (x1, y1, x2, y2) 和 (x1', y1', x2', y2') 两个子矩阵中部分坐标不同（如：x1 != x1'），那么这两个子矩阵也不同。



示例 1：

输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
输出：4
解释：四个只含 0 的 1x1 子矩阵。
示例 2：

输入：matrix = [[1,-1],[-1,1]], target = 0
输出：5
解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。


提示：

1 <= matrix.length <= 300
1 <= matrix[0].length <= 300
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
"""
import collections
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        前缀和矩阵优化O(n^3)
        @param matrix:
        @param target:
        @return:
        """
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] + matrix[i][j] - pre[i][j]
        print(pre)
        res = 0
        dic = collections.defaultdict(lambda: 0)
        for i in range(m + 1):
            for j in range(i + 1, m + 1):
                dic.clear()
                dic[0] = 1
                for k in range(1, n + 1):
                    tmp = pre[j][k] - pre[i][k]
                    if tmp - target in dic:
                        res += dic[tmp - target]
                    dic[tmp] += 1

        return res


if __name__ == '__main__':
    matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    target = 0
    print(Solution().numSubmatrixSumTarget(matrix, target))
