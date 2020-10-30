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
    def solveSudoku1(self, board: List[List[str]]) -> None:
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

    def solveSudoku2(self, board: List[List[str]]) -> None:
        """
        思路：回溯法
        1. 选出需要填表的坐标进行回溯
        2. 分别记录行、列和九宫格内数字是否被选过
        3. 当表格中所有空格都被填完，标记valid并返回，因为没有复原状态，所以返回后board的值就是填满后的值
        """
        row = [[0] * 10 for _ in range(9)]
        col = [[0] * 10 for _ in range(9)]
        box = [[0] * 10 for _ in range(9)]
        fill = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    row[i][num] = 1
                    col[j][num] = 1
                    box[i // 3 * 3 + j // 3][num] = 1
                else:
                    fill.append((i, j))

        def backtrack(index):
            # backtrack
            if index == len(fill):
                self.valid = True
                return
            i, j = fill[index]
            for num in range(1, 10):
                if row[i][num] == 0 and col[j][num] == 0 and box[i // 3 * 3 + j // 3][num] == 0:
                    row[i][num] = 1
                    col[j][num] = 1
                    box[i // 3 * 3 + j // 3][num] = 1
                    board[i][j] = str(num)
                    backtrack(index + 1)
                    if self.valid:
                        return
                    board[i][j] = "."
                    row[i][num] = 0
                    col[j][num] = 0
                    box[i // 3 * 3 + j // 3][num] = 0

        self.valid = False
        backtrack(0)
        return board

    def solveSudoku3(self, board: List[List[str]]) -> None:
        """
        思路：位运算
        1. 构造9位的二进制，判断数字是否出现过
        @param board:
        @return:
        """

        def flip(i: int, j: int, digit: int):
            line[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return

            i, j = spaces[pos]
            mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
            while mask:
                digitMask = mask & (-mask)
                digit = bin(digitMask).count("0") - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1)
                if valid:
                    return

        line = [0] * 9
        column = [0] * 9
        block = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)

        dfs(0)
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
    print(Solution().solveSudoku1(board))
    print(Solution().solveSudoku2(board))
    print(Solution().solveSudoku3(board))
