'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        执行用时 :84 ms, 在所有 Python3 提交中击败了54.93%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.97%的用户
        思路：用两个数组分别存储值为零的x,y
        时间复杂度：O(MN)
        空间复杂度：O(MN)
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix
        row, col = len(matrix), len(matrix[0])
        # O(m+n)
        arr_x, arr_y = [], []
        for i in range(row):
            if 0 in matrix[i]:
                arr_x.append(i)
                for j in range(col):
                    if matrix[i][j] == 0 and j not in arr_y:
                        arr_y.append(j)

        for i in range(row):
            if i in arr_x:
                matrix[i] = [0] * col
            else:
                for j in range(col):
                    if j in arr_y:
                        matrix[i][j] = 0

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了97.76%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.97%的用户
        :param matrix:
        :return:
        '''
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix
        row, col = len(matrix), len(matrix[0])
        # O(m+n)
        arr_x, arr_y = [], []
        for i in range(row):
            if 0 in matrix[i]:
                for j in range(col):
                    if matrix[i][j] == 0 and j not in arr_y:
                        arr_y.append(j)
                matrix[i] = [0] * col
            else:
                arr_x.append(i)

        for i in arr_x:
            for j in arr_y:
                matrix[i][j] = 0


    def setZeroes3(self, matrix: List[List[int]]) -> None:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了93.69%的用户
        内存消耗 :14.1 MB, 在所有 Python3 提交中击败了5.97%的用户
        思路：通过第一行记录是否这一列有0，后面的行如果有0，先记录列，最后将这行全置为零
        时间复杂度：O(MN)
        空间复杂度：O(1)
        :param matrix:
        :return:
        '''
        """
        Do not return anything, modify matrix in-place instead.
        """
        # if len(matrix)==0:
        #     return matrix
        flag_row = False

        row = len(matrix)
        col = len(matrix[0])

        if 0 in matrix[0]:
            flag_row = True
        for i in range(1, row):
            if 0 in matrix[i]:
                for j in range(col):
                    if matrix[i][j] == 0:
                        matrix[0][j] = 0
                matrix[i] = [0] * col

        for j in range(col):
            if matrix[0][j] == 0:
                for i in range(row):
                    matrix[i][j] = 0

        if flag_row == True:
            matrix[0] = [0] * col

