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
        """
        思路：
        1. 利用zip来
        """
        res = []
        while len(matrix):
            res += matrix[0]
            matrix.pop(0)
            print(matrix)
            matrix[::] = list(zip(*matrix))[::-1]
            print(matrix)
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

    def spiralorder3(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])  # 行，列

        # 1. 横向遍历m，纵向遍历n-1；
        # 2. 横向遍历m-1，纵向遍历n-2；
        # 3. 横向遍历m-2，纵向遍历n-3；
        # 4. 直到有一方向遍历长度为0时终止。

        ans = []
        judge = 1  # 1为顺序遍历，-1为逆序遍历
        i, j = 0, -1  # 初始位置，列为-1，因为代表[0,0]前一个位置
        while m > 0 and n > 0:

            # 横向遍历
            for x in range(n):
                j += judge * 1
                ans.append(matrix[i][j])

            # 纵向遍历
            for y in range(m - 1):
                i += judge * 1
                ans.append(matrix[i][j])

            m, n = m - 1, n - 1
            judge *= -1

        return ans


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    print(s.spiralorder(matrix))
