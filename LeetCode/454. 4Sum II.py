'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # 遍历A， B 计算A， B 所有元素两两相加的和， 并将计算结果存入 dict sumNum 中， sumNum 的 k 为和的数值， v 为两元素相加和为 k 的数量
        sumNum = collections.defaultdict(lambda: 0)
        res = 0
        for a in A:  # 时间复杂度 O(n²)
            for b in B:
                sumNum[a + b] += 1

        # 计算 C， D 的和为 k , 并检查 sumNum 中是否存在 -k， 存在则累计 sumNum[-k]
        for c in C:
            for d in D:
                k = c + d
                if -k in sumNum:  # -k 存在则 -k + k 即为 0
                    res += sumNum[-k]
        return res
