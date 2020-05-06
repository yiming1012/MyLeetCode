'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    # self.arr = []
    def solve(self, board: List[List[str]]) -> None:
        '''
        执行用时 :144 ms, 在所有 Python3 提交中击败了76.28%的用户
        内存消耗 :60.1 MB, 在所有 Python3 提交中击败了5.11%的用户
        :param board:
        :return:
        '''
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return []

        row = len(board)
        col = len(board[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]

        # print(visited)

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or visited[i][j] == 1 or board[i][j] == 'X':
                return 0
            visited[i][j] = 1
            self.arr.append([i, j])
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            # print("aaa:",self.arr)

        for i in range(row):
            for j in range(col):
                self.arr = []
                dfs(i, j)
                # print("arr:",self.arr)
                flag = 0
                for num in self.arr:
                    if num[0] in [0, row - 1] or num[1] in [0, col - 1]:
                        flag = 1
                if flag == 0:
                    for num in self.arr:
                        # print("abc:",num[0],num[1])
                        board[num[0]][num[1]] = 'X'

        return board


if __name__ == '__main__':
    board = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "X"]]
    s = Solution()
    print(s.solve(board))
