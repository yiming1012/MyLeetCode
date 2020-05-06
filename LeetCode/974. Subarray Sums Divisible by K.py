'''
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        '''
        执行用时 :404 ms, 在所有 Python3 提交中击败了40.14%的用户
        内存消耗 :17.6 MB, 在所有 Python3 提交中击败了11.11%的用户
        :param A:
        :param K:
        :return:
        '''
        count = 0
        dic = {0: 1}
        A.insert(0, 0)
        for i in range(1, len(A)):
            A[i] += A[i - 1]
            A[i] %= K
            if A[i] in dic:
                count += dic[A[i]]
                dic[A[i]] += 1
            else:
                dic[A[i]] = 1
        return count

    def subarraysDivByK2(self, A: List[int], K: int) -> int:
        pre_sum, result = 0, 0
        dic = {0: 1}  # initial

        for val in A:
            pre_sum = (pre_sum + val) % K
            if pre_sum in dic:
                result += dic[pre_sum]
                # key不存在 則默認val=0 + 1 、key在 則 val +=1
            dic[pre_sum] = dic.get(pre_sum, 0) + 1

        return result


if __name__ == '__main__':
    A = [4, 5, 0, -2, -3, 1]
    K = 5
    s = Solution()
    print(s.subarraysDivByK2(A, K))
