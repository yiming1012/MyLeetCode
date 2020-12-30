"""
1301. 最大得分的路径数目
给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。

你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍 'X'。在每一步移动中，你可以向上、向左或者左上方移动，可以移动的前提是到达的格子没有障碍。

一条路径的 「得分」 定义为：路径上所有数字的和。

请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。

如果没有任何路径可以到达终点，请返回 [0, 0] 。



示例 1：

输入：board = ["E23","2X2","12S"]
输出：[7,1]
示例 2：

输入：board = ["E12","1X1","21S"]
输出：[4,2]
示例 3：

输入：board = ["E11","XXX","11S"]
输出：[0,0]


提示：

2 <= board.length == board[i].length <= 100
"""
from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10 ** 9 + 7
        n = len(board)
        f = [[0] * n for _ in range(n)]
        g = [[0] * n for _ in range(n)]
        g[-1][-1] = 1

        def update(x, y, i, j):
            if i >= n or j >= n: return
            if board[i][j] != "X":
                if f[x][y] == f[i][j]:
                    g[x][y] = (g[x][y] + g[i][j]) % mod
                elif f[x][y] < f[i][j]:
                    f[x][y] = f[i][j]
                    g[x][y] = g[i][j]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i == n - 1 and j == n - 1) or board[i][j] == "X": continue
                update(i, j, i + 1, j)
                update(i, j, i, j + 1)
                update(i, j, i + 1, j + 1)

                if i == 0 and j == 0: break
                if board[i][j] != "S":
                    f[i][j] += int(board[i][j])

        return [f[0][0], g[0][0]] if g[0][0] > 0 else [0, 0]


if __name__ == '__main__':
    board = ["E23", "2X2", "12S"]
    print(Solution().pathsWithMaxScore(board))
