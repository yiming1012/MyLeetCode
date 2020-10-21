"""
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。

如果不含有 “山脉” 则返回 0。

 

示例 1：

输入：[2,1,4,7,3,2,5]
输出：5
解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
示例 2：

输入：[2,2,2]
输出：0
解释：不含 “山脉”。
 

提示：

0 <= A.length <= 10000
0 <= A[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-mountain-in-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        """
        思路：动态规划法
        1. up：数组，up[i]表示以i点为终点左边连续上升的山峰的个数
        2. down：数组，down[i]表示以i为终点右边连续上升的山峰的个数
        3. res：记录山脉的最大长度up[i]+down[i]-1
        @param A:
        @return:
        """
        if not A:
            return 0
        n = len(A)
        up = [1] * n
        down = [1] * n
        for i in range(1, n):
            if A[i] > A[i - 1]:
                up[i] = up[i - 1] + 1

            if A[n - i - 1] > A[n - i]:
                down[n - i - 1] = down[n - i] + 1

        res = 0
        for i in range(1, n - 1):
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                res = max(res, up[i] + down[i] - 1)
        return res


if __name__ == '__main__':
    A = [2, 1, 4, 7, 3, 2, 5]
    print(Solution().longestMountain(A))
