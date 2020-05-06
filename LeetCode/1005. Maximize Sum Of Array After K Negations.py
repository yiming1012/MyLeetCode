'''
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
 

Note:

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        '''
        执行用时 :68 ms, 在所有 Python3 提交中击败了61.61%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了20.00%的用户
        :param A:
        :param K:
        :return:
        '''
        A.sort()
        # 负数变为正数
        # 如果可仍然大于0，获取最小值，进行状态变化
        for i in range(len(A)):
            if A[i] < 0 and K > 0:
                A[i] = -A[i]
                K -= 1
            else:
                break
        if K > 0:
            return sum(A) if K % 2 == 0 else sum(A) - 2 * min(A)
        else:
            return sum(A)

    def largestSumAfterKNegations2(self, A: List[int], K: int) -> int:
        '''
        简单粗暴
        :param A:
        :param K:
        :return:
        '''
        for i in range(K):
            A.sort()
            A[0] = -A[0]
        return sum(A)

