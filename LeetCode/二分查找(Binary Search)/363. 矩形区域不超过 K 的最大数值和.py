"""
363. 矩形区域不超过 K 的最大数值和
给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。

题目数据保证总会存在一个数值和不超过 k 的矩形区域。

 

示例 1：


输入：matrix = [[1,0,1],[0,-2,3]], k = 2
输出：2
解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
示例 2：

输入：matrix = [[2,2,-1]], k = 3
输出：3
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105
 

进阶：如果行数远大于列数，该如何设计解决方案？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from bisect import bisect
from typing import List

from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        思路：
        1. 先计算二维前缀和presum
        2. 固定上下界，列坐标从左至右扫描，找到presum[j+1][r]-presum[i][l]<=k的最大值，即presum[i][l] >= presum[j+1][r]-k的最大值
        我们先将presum[j+1][r]-k有序插入arr中，每次遍历一个值后再arr中二分查找
        @param matrix:
        @param k:
        @return:
        """
        m, n = len(matrix), len(matrix[0])
        presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                presum[i + 1][j + 1] = presum[i][j + 1] + presum[i + 1][j] + matrix[i][j] - presum[i][j]
        print(presum)
        res = float('-inf')
        # presum[i][r]-presum[i][l]<=k
        # 枚举上行
        for i in range(m):
            # 枚举下行
            for j in range(i, m):
                arr = [0]
                for r in range(n):
                    t = presum[j + 1][r + 1] - presum[i][r + 1]
                    index = bisect.bisect_left(arr, t - k)
                    if index < len(arr):
                        res = max(res, t - arr[index])
                    bisect.insort(arr, t)
        return res


if __name__ == '__main__':
    matrix = [[1, 0, 1], [0, -2, 3]]
    k = 2
    print(Solution().maxSumSubmatrix(matrix, k))
