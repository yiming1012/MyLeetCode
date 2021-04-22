"""
417. 太平洋大西洋水流问题
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

 

提示：

输出坐标的顺序不重要
m 和 n 都小于150
 

示例：

 

给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        思路：顺流而下
        1. 从大陆开始流向太平洋和大西洋，通过两位二进制记录最终流向，如果能流向太平洋，ans |=2,如果能流向大西洋，ans |=1
            1. 00：都不能流入
            2. 01：能流向大西洋
            3. 10：能流向太平洋
            4. 11：能流向太平洋和大西洋
        2. 当某个点对应的ans=3时，说明既能流向太平洋也能流向大西洋
        @param heights:
        @return:
        """
        m, n = len(heights), len(heights[0])
        pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            visited.add((x, y))

            ans = 0
            if x == 0 or y == 0:
                ans |= 2
            if x == m - 1 or y == n - 1:
                ans |= 1
            print(x, y, ans)

            for dx, dy in pos:
                xx, yy = x + dx, y + dy
                if 0 <= xx < m and 0 <= yy < n and heights[xx][yy] <= heights[x][y] and (xx, yy) not in visited:
                    ans |= dfs(xx, yy)
            print(x, y, ans)
            memo[(x, y)] = ans
            return ans

        memo = {}
        res = []
        visited = set()
        for i in range(m):
            for j in range(n):
                visited.clear()
                if dfs(i, j) == 3:
                    res.append((i, j))

        return res

    def pacificAtlantic2(self, heights: List[List[int]]) -> List[List[int]]:
        """
        逆向思维：从边界开始查找里面分别流向太平洋和大西洋的水流
        @param heights:
        @return:
        """
        m, n = len(heights), len(heights[0])
        pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, arr):
            arr[x][y] = 1
            for dx, dy in pos:
                xx, yy = x + dx, y + dy
                if 0 <= xx < m and 0 <= yy < n and heights[xx][yy] >= heights[x][y] and not arr[xx][yy]:
                    dfs(xx, yy, arr)

        Pacific = [[0] * n for _ in range(m)]
        Atlantic = [[0] * n for _ in range(m)]

        for i in range(n):
            dfs(0, i, Pacific)
            dfs(m - 1, i, Atlantic)
        for j in range(m):
            dfs(j, 0, Pacific)
            dfs(j, n - 1, Atlantic)

        res = []
        for i in range(m):
            for j in range(n):
                if Pacific[i][j] and Atlantic[i][j]:
                    res.append([i, j])
        return res


if __name__ == '__main__':
    heights = [[1, 1], [1, 1], [1, 1]]
    print(Solution().pacificAtlantic(heights))
    print(Solution().pacificAtlantic2(heights))
