'''
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:

Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

Constraints:

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        '''
        执行用时 :72 ms, 在所有 Python3 提交中击败了96.60%的用户
        内存消耗 :18.8 MB, 在所有 Python3 提交中击败了98.29%的用户
        :param A:
        :return:
        '''
        if len(A) < 3:
            return False

        if sum(A) % 3 == 0:
            div = sum(A) // 3
            i, j = 0, len(A) - 1
            sumleft = sumright = 0
            while i < j - 1:
                if sumleft + A[i] != div:
                    sumleft += A[i]
                    i += 1
                if sumright + A[j] != div:
                    sumright += A[j]
                    j -= 1

                if sumleft + A[i] == div and sumright + A[j] == div:
                    if i < j - 1:
                        return True
                    else:
                        return False
        return False

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        '''
        执行用时 :76 ms, 在所有 Python3 提交中击败了96.37%的用户
        内存消耗 :18.7 MB, 在所有 Python3 提交中击败了98.29%的用户
        :param A:
        :return:
        '''
        if len(A) < 3:
            return False

        if sum(A) % 3 != 0:
            return False

        target = sum(A) // 3
        num = 0
        sumValue = 0
        for i in A:
            sumValue += i
            if sumValue == target:
                sumValue = 0
                num += 1
        return num >= 3

'''
方法一：利用双指针从后往前遍历，如果两块都等于target的值，且中间还有一段就返回True
方法二：一次遍历，遇到和为target，记录一次，num大于等于3，可能和为0
'''
if __name__ == '__main__':
    A = [1, -1, 0, 1, -1]
    s = Solution()
    print(s.canThreePartsEqualSum(A))
