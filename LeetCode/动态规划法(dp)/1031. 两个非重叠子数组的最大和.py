"""
给出非负整数数组 A ，返回两个非重叠（连续）子数组中元素的最大和，子数组的长度分别为 L 和 M。（这里需要澄清的是，长为 L 的子数组可以出现在长为 M 的子数组之前或之后。）

从形式上看，返回最大的 V，而 V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) 并满足下列条件之一：

 

0 <= i < i + L - 1 < j < j + M - 1 < A.length, 或
0 <= j < j + M - 1 < i < i + L - 1 < A.length.
 

示例 1：

输入：A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
输出：20
解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
示例 2：

输入：A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
输出：29
解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
示例 3：

输入：A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
输出：31
解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。
 

提示：

L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-sum-of-two-non-overlapping-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)

        def countSum(L, M):
            print(L,M)
            preSumL = 0
            preSumM = 0

            dpL = [0] * n
            dpM = [0] * n
            for i in range(n - M):
                preSumL += A[i]
                if i >= L - 1:
                    dpL[i] = max(dpL[i - 1], preSumL)
                    preSumL -= A[i - L + 1]
            print(dpL)

            for i in range(n - 2, L-2, -1):
                preSumM += A[i+1]
                if i <= n - M - 1:
                    dpM[i] = max(dpM[i + 1], preSumM)
                    preSumM -= A[i + M]
            print(dpM)

            res = 0
            for i in range(L - 1, n - M):
                res = max(dpL[i] + dpM[i], res)
            return res

        return max(countSum(L, M), countSum(M, L))

    def maxSumTwoNoOverlap2(self, A: List[int], L: int, M: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        print(A)
        res = A[L + M - 1]
        Lmax = A[L - 1]
        Mmax = A[M - 1]
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, max(Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L]))

        return res


if __name__ == '__main__':
    A = [67, 38, 92, 21, 91, 24, 25, 20, 100, 41, 22, 56, 63, 42, 95, 76, 84, 79, 89, 3]
    L = 3
    M = 4
    print(A)

    print(Solution().maxSumTwoNoOverlap(A, L, M))
    print(Solution().maxSumTwoNoOverlap2(A, L, M))
