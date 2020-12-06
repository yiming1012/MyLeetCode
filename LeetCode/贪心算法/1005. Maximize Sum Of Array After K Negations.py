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
import heapq
from typing import List


class Solution:
    def largestSumAfterKNegations1(self, A: List[int], K: int) -> int:
        '''
        执行用时 :68 ms, 在所有 Python3 提交中击败了61.61%的用户
        内存消耗 :13.8 MB, 在所有 Python3 提交中击败了20.00%的用户
        :param A:
        :param K:
        :return:
        '''
        # 负数变为正数
        # 如果可仍然大于0，获取最小值，进行状态变化
        A.sort()
        for i, a in enumerate(A):
            if a >= 0 or K <= 0:
                break
            A[i] = -a
            K -= 1
        if K % 2:
            return sum(A) - 2 * min(A)
        return sum(A)

    def largestSumAfterKNegations2(self, A: List[int], K: int) -> int:
        """
        思路：每次修改堆顶元素
        @param A:
        @param K:
        @return:
        """
        heapq.heapify(A)
        while K:
            min_ = heapq.heappop(A)
            heapq.heappush(A, -min_)
            K -= 1
        return sum(A)


if __name__ == '__main__':
    A = [4, 2, 3]
    K = 1
    print(Solution().largestSumAfterKNegations1(A, K))
    print(Solution().largestSumAfterKNegations2(A, K))
