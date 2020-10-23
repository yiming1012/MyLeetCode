"""
对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得：

对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。

那么数组 A 是漂亮数组。

 

给定 N，返回任意漂亮数组 A（保证存在一个）。

 

示例 1：

输入：4
输出：[2,1,4,3]
示例 2：

输入：5
输出：[3,1,2,5,4]
 

提示：

1 <= N <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/beautiful-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        """
        思路：分治法
        1. 比如1 2 3 4 5 通过奇偶先将135 24分开 再将135分为15 3
        @param N:
        @return:
        """
        def dfs(arr):
            if len(arr) <= 2:
                return arr
            # 获取奇数位
            odd = dfs(arr[1::2])
            # 获取偶数位
            even = dfs(arr[::2])
            # 将奇偶并列
            return odd + even

        A = list(range(1, N + 1))
        return dfs(A)
