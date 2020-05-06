'''
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

 

Example 1:



Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
In this example the rook is able to capture all the pawns.
Example 2:



Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation:
Bishops are blocking the rook to capture any pawn.
Example 3:



Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
The rook can capture the pawns at positions b5, d6 and f5.
 

Note:

board.length == board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/available-captures-for-rook
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了60.20%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.26%的用户
        :param board:
        :return:
        '''
        # print(board)
        if len(board) == 0:
            return 0
        count = 0
        flag = 0
        row, col = 0, 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print(board[i][j])
                if board[i][j] == 'R':
                    # print(i,j)
                    row, col = i, j
                    flag = 1
                    break
            if flag == 1:
                break

        while True:
            if row > 0:
                for i in range(row - 1, -1, -1):
                    # print(i,col)
                    if board[i][col] == 'B':
                        break
                    if board[i][col] == 'p':
                        count += 1
                        break

            if row < len(board) - 1:
                for i in range(row + 1, len(board)):
                    # print(i,col)
                    if board[i][col] == 'B':
                        break
                    if board[i][col] == 'p':
                        count += 1
                        break

            if col > 0:
                for i in range(col - 1, -1, -1):
                    # print(row,i)
                    if board[row][i] == 'B':
                        break
                    if board[row][i] == 'p':
                        count += 1
                        break

            if col < len(board) - 1:
                for i in range(col + 1, len(board)):
                    # print(row,i)
                    if board[row][i] == 'B':
                        break
                    if board[row][i] == 'p':
                        count += 1
                        break
            break

        return count

    def numRookCaptures1(self, board: List[List[str]]) -> int:
        '''
        执行用时 :48 ms, 在所有 Python3 提交中击败了24.49%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.26%的用户
        :param board:
        :return:
        '''
        for i in range(len(board)):
            if 'R' in board[i]:
                x = i
                y = board[i].index('R')
                break
        print(x, y)
        row = ''.join(board[x]).replace('.', '')
        print(row)
        col = ''.join(row[y] for row in board).replace('.', '')
        print(col)

        return row.count('Rp') + row.count('pR') + col.count('Rp') + col.count('pR')


if __name__ == '__main__':
    board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
             [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
    s = Solution()
    print(s.numRookCaptures1(board))
