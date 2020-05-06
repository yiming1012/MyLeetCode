'''
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 

Note:

1 <= N <= 50
0 <= grid[i][j] <= 50

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        '''
        执行用时 :112 ms, 在所有 Python3 提交中击败了62.65%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.77%的用户
        思路：总立方体的表面积和-所有相邻面的个数*2，即num*6-(x+y+z)*2
        :param grid:
        :return:
        '''
        x = y = z = num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(grid[i][j])
                num += grid[i][j]
                if grid[i][j] > 1:
                    z += grid[i][j] - 1
                if i > 0:
                    x += min(grid[i][j], grid[i - 1][j])
                if j > 0:
                    y += min(grid[i][j], grid[i][j - 1])
        print(x, y, z, num)
        return num * 6 - (x + y + z) * 2


if __name__ == '__main__':
    # grid = [[2]]
    # grid = [[1, 2], [3, 4]]
    grid = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    s = Solution()
    print(s.surfaceArea(grid))
