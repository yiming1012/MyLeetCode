"""
962. 最大宽度坡
给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。

找出 A 中的坡的最大宽度，如果不存在，返回 0 。

 

示例 1：

输入：[6,0,8,2,1,5]
输出：4
解释：
最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
示例 2：

输入：[9,8,1,0,1,9,4,0,4,1]
输出：7
解释：
最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
 

提示：

2 <= A.length <= 50000
0 <= A[i] <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-width-ramp
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxWidthRamp1(self, A: List[int]) -> int:
        """
        求一个最长的上坡
        索引排序
        @param A:
        @return:
        """
        n = len(A)
        indices = sorted(range(n), key=lambda i: A[i])
        res = 0
        pre = n
        for i in indices:
            if i < pre:
                pre = i
            else:
                res = max(res, i - pre)
        return res

    def maxWidthRamp2(self, A: List[int]) -> int:
        """
        单调栈
        @param A:
        @return:
        """
        stack = []
        for i, a in enumerate(A):
            if not stack or (stack and A[stack[-1]] > a):
                stack.append(i)

        res = 0
        for i in range(len(A) - 1, -1, -1):
            while stack and A[stack[-1]] <= A[i]:
                res = max(res, i - stack.pop())

        return res


if __name__ == '__main__':
    A = [6, 0, 8, 2, 1, 5]
    print(Solution().maxWidthRamp1(A))
    print(Solution().maxWidthRamp2(A))
