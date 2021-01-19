"""
1197. 进击的骑士
一个坐标可以从 -infinity 延伸到 +infinity 的 无限大的 棋盘上，你的 骑士 驻扎在坐标为 [0, 0] 的方格里。

骑士的走法和中国象棋中的马相似，走 “日” 字：即先向左（或右）走 1 格，再向上（或下）走 2 格；或先向左（或右）走 2 格，再向上（或下）走 1 格。

每次移动，他都可以按图示八个方向之一前进。



现在，骑士需要前去征服坐标为 [x, y] 的部落，请你为他规划路线。

最后返回所需的最小移动次数即可。本题确保答案是一定存在的。



示例 1：

输入：x = 2, y = 1
输出：1
解释：[0, 0] → [2, 1]
示例 2：

输入：x = 5, y = 5
输出：4
解释：[0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]


提示：

|x| + |y| <= 300
"""
import collections


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        思路：朴素BFS，遍历八个方向
        @param x:
        @param y:
        @return:
        """
        pos = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        queue = collections.deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))
        step = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == x and j == y:
                    return step
                for dx, dy in pos:
                    ix, jy = i + dx, j + dy
                    if (ix, jy) not in visited:
                        visited.add((ix, jy))
                        queue.append((ix, jy))
            step += 1
        return


if __name__ == '__main__':
    x = 2
    y = 1
    print(Solution().minKnightMoves(x, y))
