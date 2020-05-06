'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def spiralorder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while len(matrix):
            res += matrix[0]
            matrix.pop(0)
            # print(matrix)
            matrix[::] = list(zip(*matrix))[::-1]
            # print(matrix)
        return res

    def spiralorder2(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        x = y = di = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        res = []
        visited = set()

        for i in range(m * n):
            res.append(matrix[x][y])
            visited.add((x, y))
            nx, ny = x + dx[di], y + dy[di]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                x, y = nx, ny
            else:
                di = (di + 1) % 4  # 如果不满足条件，换一个方向进行遍历
                x, y = x + dx[di], y + dy[di]
        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    print(s.spiralOrder(matrix))
