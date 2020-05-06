'''
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

 

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1
 

Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-turbulent-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        '''
        
        :param A:
        :return:
        '''
        n = len(A)
        if n <= 1:
            return n

        flag = 0
        count = 1
        res = 0

        for i in range(n - 1):
            if A[i] > A[i + 1] and flag == -1:
                flag = 1
                count += 1
            elif A[i] < A[i + 1] and flag == 1:
                flag = -1
                count += 1
            elif A[i] == A[i + 1]:
                res = max(res, count)
                count = 1
            else:
                res = max(res, count)
                if A[i] > A[i + 1]:
                    flag = 1
                    count = 2
                elif A[i] < A[i + 1]:
                    flag = -1
                    count = 2
                else:
                    count = 1
            if i == n - 2:
                res = max(res, count)

        return res



    def maxTurbulenceSize2(self, A: List[int]) -> int:
        tmp = 0
        res = 0
        flag = 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and flag == 1:
                flag = 0
                tmp += 1
                res = max(res, tmp)
            elif A[i] < A[i - 1] and flag == 0:
                flag = 1
                tmp += 1
                res = max(res, tmp)
            elif A[i] == A[i - 1]:
                tmp = 0
            else:
                tmp = 1
        return res + 1
