'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/magic-squares-in-grid
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        '''
        执行用时 :64 ms, 在所有 Python3 提交中击败了14.46%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了6.67%的用户
        :param grid:
        :return:
        '''
        if len(grid)<3 or len(grid[0])<3:
            return 0
        row = len(grid)
        col =len(grid[0])
        count = 0
        array = [i for i in range(1,10)]
        for i in range(row-2):
            for j in range(col-2):
                arr =[]
                # print(i,j)
                arr.extend(grid[i][j:j+3])
                arr.extend(grid[i+1][j:j+3])
                arr.extend(grid[i+2][j:j+3])
                arr.sort()
                # print(arr)
                # print(sum(grid[i][j:j+3]))
                if arr!=array or grid[i+1][j+1]!=5 or sum(grid[i][j:j+3])!=15 or sum(grid[i+1][j:j+3])!=15 or sum(grid[i+2][j:j+3])!=15 or grid[i][j]+grid[i+1][j]+grid[i+2][j]!=15 or grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]!=15:
                    continue
                else:
                    count+=1
        return count