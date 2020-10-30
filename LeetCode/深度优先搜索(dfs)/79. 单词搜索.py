"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 

提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dic = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        wc = len(word)

        def dfs(x, y, visited, index):
            if index == wc - 1:
                return True

            for i in range(4):
                a, b = dic[i]
                if 0 <= x + a < m and 0 <= y + b < n and not visited[x + a][y + b] and index + 1 < wc and board[x + a][
                    y + b] == word[index + 1]:
                    visited[x + a][y + b] = 1
                    if dfs(x + a, y + b, visited, index + 1):
                        return True
                    visited[x + a][y + b] = 0
            return False

        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if dfs(i, j, visited, 0):
                        return True
                    visited[i][j] = 0
        return False

    def exist2(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        def dfs(index, start_x, start_y, marked):
            # 先写递归终止条件
            if index == len(word) - 1:
                return board[start_x][start_y] == word[index]

            # 中间匹配了，再继续搜索
            if board[start_x][start_y] == word[index]:
                # 先占住这个位置，搜索不成功的话，要释放掉
                marked[start_x][start_y] = True
                for direction in directions:
                    new_x = start_x + direction[0]
                    new_y = start_y + direction[1]
                    # 注意：如果这一次 search word 成功的话，就返回
                    if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y] and dfs(index + 1, new_x, new_y,
                                                                                              marked):
                        return True
                marked[start_x][start_y] = False
            return False

        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 对每一个格子都从头开始搜索
                if dfs(0, i, j, marked):
                    return True
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))
    print(Solution().exist2(board, word))
