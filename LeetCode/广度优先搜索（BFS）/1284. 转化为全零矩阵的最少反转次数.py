"""
1284. 转化为全零矩阵的最少反转次数
给你一个 m x n 的二进制矩阵 mat。

每一步，你可以选择一个单元格并将它反转（反转表示 0 变 1 ，1 变 0 ）。如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。（注：相邻的两个单元格共享同一条边。）

请你返回将矩阵 mat 转化为全零矩阵的最少反转次数，如果无法转化为全零矩阵，请返回 -1 。

二进制矩阵的每一个格子要么是 0 要么是 1 。

全零矩阵是所有格子都为 0 的矩阵。

 

示例 1：



输入：mat = [[0,0],[0,1]]
输出：3
解释：一个可能的解是反转 (1, 0)，然后 (0, 1) ，最后是 (1, 1) 。
示例 2：

输入：mat = [[0]]
输出：0
解释：给出的矩阵是全零矩阵，所以你不需要改变它。
示例 3：

输入：mat = [[1,1,1],[1,0,1],[0,0,0]]
输出：6
示例 4：

输入：mat = [[1,0,0],[1,0,0]]
输出：-1
解释：该矩阵无法转变成全零矩阵
 

提示：

m == mat.length
n == mat[0].length
1 <= m <= 3
1 <= n <= 3
mat[i][j] 是 0 或 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from copy import deepcopy
from typing import List


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        size = row * col
        queue = collections.deque()
        upack = lambda m: [e for sub in m for e in sub]
        visited = set()
        start = upack(mat)
        queue.append(tuple(start))
        visited.add(tuple(start))
        directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        while queue:
            for _ in range(len(queue)):
                node = list(queue.popleft())
                if all(num == 0 for num in node):
                    return ans
                for i in range(size):
                    node_copy = node.copy()
                    r, c = i // col, i % col
                    for x, y in directions:
                        if 0 <= r + x < row and 0 <= c + y < col:
                            index = (r + x) * col + (c + y)
                            node_copy[index] ^= 1
                    if tuple(node_copy) not in visited:
                        visited.add(tuple(node_copy))
                        queue.append(tuple(node_copy))

            ans += 1
        return -1


if __name__ == '__main__':
    mat = [[0, 0], [0, 1]]
    print(Solution().minFlips(mat))
