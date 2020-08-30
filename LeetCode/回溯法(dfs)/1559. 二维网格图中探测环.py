"""
给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。

一个环是一条开始和结束于同一个格子的长度 大于等于 4 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 相同的值 。

同时，你也不能回到上一次移动时所在的格子。比方说，环  (1, 1) -> (1, 2) -> (1, 1) 是不合法的，因为从 (1, 2) 移动到 (1, 1) 回到了上一次移动时的格子。

如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。

 

示例 1：



输入：grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
输出：true
解释：如下图所示，有 2 个用不同颜色标出来的环：

示例 2：



输入：grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
输出：true
解释：如下图所示，只有高亮所示的一个合法环：

示例 3：



输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
输出：false
 

提示：

m == grid.length
n == grid[i].length
1 <= m <= 500
1 <= n <= 500
grid 只包含小写英文字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/detect-cycles-in-2d-grid
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import sys
from typing import List

sys.setrecursionlimit(999999999)


class Solution:
    def containsCycle1(self, grid: List[List[str]]) -> bool:
        """
        思路：DFS
        1. 找环时，不退回到上一步，如果访问到一点已经访问过，说明存在环
        2. 由于Python递归深度998，所以需要修改递归深度

        @param grid:
        @return:
        """
        m = len(grid)
        n = len(grid[0])
        # 记录（i, j）位置是否被访问过，0表示未访问过。
        vis = [[0] * n for _ in range(m)]

        # 方向数组
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def dfs(x, y, p):
            # p表示遍历的方向。
            # 先将x,y标记为已经访问过
            vis[x][y] = 1
            # 遍历四个方向
            for i in range(4):
                # 如果当前的遍历的方向等于来时的方向，说明往回走了，
                # 所以在当前遍历的方向不等于来时的方向时，进行下一步
                if i != p:
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    # 如果新的位置没有越界，并且grid[x][y] = grid[new_x][new_y]
                    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and grid[new_x][new_y] == grid[x][y]:
                        # 如果(newx, new_y) 已经访问过了，说明找到了环
                        # print(vis[new_x][new_y])
                        if vis[new_x][new_y]:
                            return True
                            # 否则对new_x, new_y进行DFS
                        # 这里的i^1比较难理解，建议看视频
                        if dfs(new_x, new_y, i ^ 1):
                            return True
            return False

        for i in range(m):
            for j in range(n):
                # 如果（i, j）没有访问过，进行DFS，-1表示初始时起点是没有路径指向它的，
                if not vis[i][j] and dfs(i, j, -1):
                    return True
        return False

    def containsCycle2(self, grid: List[List[str]]) -> bool:
        """
        思路：并查集
        1. 先初始化parent列表，将二维数组的下标志指向自己，通过for循环构成
        2. 并查集用到了find和union函数，分别查找根节点和合并两个集合
        3. 如果某一次两个点的根节点相同，说明存在环
        @param grid:
        @return:
        """
        m, n = len(grid), len(grid[0])
        parent = [i for i in range(m * n)]

        def find(root):
            if root != parent[root]:
                parent[root] = find(parent[root])
            return parent[root]

        def union(a, b):
            a_parent = find(a)
            b_parent = find(b)
            if a_parent == b_parent:
                return True
            else:
                parent[b_parent] = a_parent
                return False

        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if union(i * n + j, (i - 1) * n + j):
                        return True
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if union(i * n + j, i * n + j - 1):
                        return True
        return False
