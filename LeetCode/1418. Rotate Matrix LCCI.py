'''
Given an image represented by an N x N matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

 

Example 1:

Given matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

Rotate the matrix in place. It becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

Rotate the matrix in place. It becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-matrix-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        执行用时 :40 ms, 在所有 Python3 提交中击败了61.50%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：借助matrix的copy
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        # if row==0:
        #     return matrix
        copyMatrix = [[_ for _ in num] for num in matrix]
        # print(copyMatrix)
        for i in range(row):
            matrix[i] = [copyMatrix[row - j][i] for j in range(1, row + 1)]
        # print(matrix)
        return matrix

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 这里必须[::]分片，不然matrix=zip(*matrix[::-1])只是浅拷贝
        matrix = list(zip(*matrix[::-1]))
        # matrix[::] = zip(*matrix[::-1])
        return matrix


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    print(s.rotate2(matrix))
