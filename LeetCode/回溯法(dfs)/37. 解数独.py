"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        col = [set() for i in range(9)]
        row = [set() for i in range(9)]
        sqr = [[set() for i in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    col[j].add(board[i][j])
                    row[i].add(board[i][j])
                    sqr[i // 3][j // 3].add(board[i][j])

        def dfs(i, j):
            if board[i][j] != '.':
                if i == 8 and j == 8:
                    self.flag = True
                    return
                if j < 8:
                    dfs(i, j + 1)
                else:
                    dfs(i + 1, 0)
                return

            for ch in range(1, 10):
                ch = str(ch)
                if ch not in col[j] and ch not in row[i] and ch not in sqr[i // 3][j // 3]:
                    col[j].add(ch)
                    row[i].add(ch)
                    sqr[i // 3][j // 3].add(ch)
                    board[i][j] = ch
                    if i == 8 and j == 8:
                        self.flag = True
                        return
                    if j < 8:
                        dfs(i, j + 1)
                    else:
                        dfs(i + 1, 0)

                    if self.flag: return
                    board[i][j] = '.'
                    col[j].remove(ch)
                    row[i].remove(ch)
                    sqr[i // 3][j // 3].remove(ch)

        self.flag = False
        dfs(0, 0)
        return board


if __name__ == '__main__':
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(Solution().solveSudoku(board))
