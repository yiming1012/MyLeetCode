'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/game-of-life
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import copy
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        '''
        执行用时 :104 ms, 在所有 Python3 提交中击败了6.56%的用户
        内存消耗 :29.1 MB, 在所有 Python3 提交中击败了10.53%的用户
        思路：利用额外的数组记录当前值，最后赋值给原数组
        1、copy.deepcopy知识点
        :param board:
        :return:
        '''
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        row, col = len(board), len(board[0])

        def fun(i, j, flag):
            dic = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
            count = 0
            for d in dic:
                x, y = i + d[0], j + d[1]
                if 0 <= x < row and 0 <= y < col:
                    if board[x][y] == 1:
                        count += 1
            if count < 2:
                flag = 0
            elif count == 3:
                flag = 1
            elif count > 3:
                flag = 0

            return flag

        arr = copy.deepcopy(board)
        for i in range(row):
            for j in range(col):
                arr[i][j] = fun(i, j, board[i][j])

        for r in range(row):
            for c in range(col):
                board[r][c] = arr[r][c]

        return board

    def gameOfLife2(self, board: List[List[int]]) -> None:
        '''
        执行用时 :144 ms, 在所有 Python3 提交中击败了5.04%的用户
        内存消耗 :29.1 MB, 在所有 Python3 提交中击败了10.53%的用户
        思路：原地修改board[i][j]的值
        规律：
        0-1：-1
        1-0；2
        :param board:
        :return:
        '''
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        row, col = len(board), len(board[0])

        def fun(i, j, flag):
            dic = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
            count = 0
            for d in dic:
                x, y = i + d[0], j + d[1]
                if 0 <= x < row and 0 <= y < col:
                    if board[x][y] >= 1:
                        count += 1
            if flag == 1:
                if count < 2 or count > 3:
                    flag = 2
            else:
                if count == 3:
                    flag = -1

            return flag

        for i in range(row):
            for j in range(col):
                board[i][j] = fun(i, j, board[i][j])

        for r in range(row):
            for c in range(col):
                if board[r][c] == -1:
                    board[r][c] = 1
                elif board[r][c] == 2:
                    board[r][c] = 0

        return board

    '''
    思路，原地修改的前提是，数字特征值记录迭代前死活，本人的思路是校验奇偶，即定义：
    状态 00： 0000 ，死的，下一轮还是死的
    状态 11： 0101，活的，下一轮死了
    状态 22： 1010，死的，下一轮活了
    状态 33： 1111，活的，下一轮继续活着

    活->活 1->1
    活->死 1->3
    死->活 0->2
    死->死 0->0
    只有死活转换的时候需要改变board值，也就是说：
    board以前是活的时候，需要判断现在是否要死过去
    board以前是死的时候，需要判断现在是否要活过来
    检查原状态的时候，只需要%2即可知道原状态，&1和%2效果一样
    计数函数，遍历九个格子，不能越界，不能原地比较：不能ij同时为0
    '''

    def gameOfLife3(self, board: List[List[int]]) -> None:
        '''
        执行用时 :100 ms, 在所有 Python3 提交中击败了6.56%的用户
        内存消耗 :28.9 MB, 在所有 Python3 提交中击败了10.53%的用户
        :param board:
        :return:
        '''
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                C = 0
                for x in (-1, 0, 1):
                    for y in (-1, 0, 1):
                        if (x or y) and 0 <= i + x < n and 0 <= j + y < m and board[x + i][j + y] & 1: C += 1
                if board[i][j] & 1 and (2 <= C <= 3): board[i][j] = 3
                if board[i][j] & 1 == 0 and C == 3: board[i][j] = 2

        for i in range(n):
            for j in range(m):
                board[i][j] >>= 1
        return board


if __name__ == '__main__':
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    s = Solution()
    print(s.gameOfLife3(board))
