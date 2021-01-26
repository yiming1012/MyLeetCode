"""
959. 由斜杠划分区域
在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。

（请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。

返回区域的数目。

 

示例 1：

输入：
[
  " /",
  "/ "
]
输出：2
解释：2x2 网格如下：

示例 2：

输入：
[
  " /",
  "  "
]
输出：1
解释：2x2 网格如下：

示例 3：

输入：
[
  "\\/",
  "/\\"
]
输出：4
解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
2x2 网格如下：

示例 4：

输入：
[
  "/\\",
  "\\/"
]
输出：5
解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
2x2 网格如下：

示例 5：

输入：
[
  "//",
  "/ "
]
输出：3
解释：2x2 网格如下：

 

提示：

1 <= grid.length == grid[0].length <= 30
grid[i][j] 是 '/'、'\'、或 ' '。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regions-cut-by-slashes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        """
        思路：将每个单元格划分为上下左右4个部分
        @param grid:
        @return:
        """
        n = len(grid)
        self.count = n * n * 4
        parent = list(range(4 * n * n))

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            x, y = find(a), find(b)
            if x != y:
                parent[y] = x
                self.count -= 1

        index = lambda i, j, k: (i * n + j) * 4 + k

        for i in range(n):
            for j in range(n):
                if i > 0:
                    union(index(i, j, 0), index(i - 1, j, 2))
                if j > 0:
                    union(index(i, j, 3), index(i, j - 1, 1))
                if grid[i][j] == '/':
                    union(index(i, j, 0), index(i, j, 3))
                    union(index(i, j, 1), index(i, j, 2))
                elif grid[i][j] == '\\':
                    union(index(i, j, 0), index(i, j, 1))
                    union(index(i, j, 2), index(i, j, 3))
                else:
                    union(index(i, j, 0), index(i, j, 1))
                    union(index(i, j, 1), index(i, j, 2))
                    union(index(i, j, 2), index(i, j, 3))
        return self.count


if __name__ == '__main__':
    grid = [" /", "/ "]
    print(Solution().regionsBySlashes(grid))
