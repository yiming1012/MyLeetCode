"""
861. 翻转矩阵后的得分
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。

 

示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

提示：

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] 是 0 或 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/score-after-flipping-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def matrixScore1(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        res = 0
        # 如果首项为0，将本列转换
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] ^= 1

        # 如果某列少于m//2,交换
        for i in range(1, n):
            ones = 0
            for j in range(m):
                if A[j][i] == 1:
                    ones += 1
            if ones < (m + 1) // 2:
                for k in range(m):
                    A[k][i] ^= 1
        # 计算最终结果
        res = 0
        for i in range(m):
            row = 0
            for j in range(n):
                row = (row << 1) + A[i][j]
            res += row
        return res

    def matrixScore2(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        # 如果首项为0，将本列转换
        for i in range(m):
            if A[i][0]: continue
            for j in range(n):
                A[i][j] ^= 1

        # 对每一列批量计算
        res = (1 << (n - 1)) * m
        for i in range(1, n):
            ones = sum(A[j][i] for j in range(m))
            ones = max(ones, m - ones)
            res += (1 << (n - i - 1)) * ones
        return res


if __name__ == '__main__':
    A = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    print(Solution().matrixScore(A))
