'''
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.



Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.


Note:

0 <= A.length <= 40000
0 <= A[i] < 40000

'''
from typing import List
import collections


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        '''
        执行用时 :748 ms, 在所有 Python3 提交中击败了18.71%的用户
        内存消耗 :18.9 MB, 在所有 Python3 提交中击败了13.64%的用户
        思路：讲数组排序之后，如果和前面的重复，就将该数变为前一个数的后一个自然数
        如：[1,1,2,2,3]
        [1,2,2,2,3] 1
        [1,2,3,2,3] 1
        [1,2,3,4,3] 2
        [1,2,3,4,5] 2
        :param A:
        :return:
        '''
        A.sort()
        print(A)
        count = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                count += A[i - 1] - A[i] + 1
                A[i] += A[i - 1] - A[i] + 1

        print(A)

        return count

    def minIncrementForUnique2(self, A: List[int]) -> int:
        count = [0] * 80000
        for x in A:
            count[x] += 1

        ans = taken = 0
        for x in range(80000):
            if count[x] >= 2:
                taken += count[x] - 1
                ans -= x * (count[x] - 1)
            elif taken > 0 and count[x] == 0:
                taken -= 1
                ans += x

        return ans

    def minIncrementForUnique3(self, A: List[int]) -> int:
        '''
        执行用时 :492 ms, 在所有 Python3 提交中击败了38.51%的用户
        内存消耗 :18.8 MB, 在所有 Python3 提交中击败了15.38%的用户
        :param A:
        :return:
        '''
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in range(1, len(A)):
            if A[i - 1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i - 1] - 1)
                ans += give * (give + 1) // 2 + give * A[i - 1]
                taken -= give

        return ans

    def minIncrementForUnique4(self, A: List[int]) -> int:
        d = collections.Counter(A)
        d = dict(d)
        kk = d.keys()
        kk = sorted(kk)
        print(kk)
        move = 0
        num = -1
        for k in kk:
            if num < k:
                num = k
            move += (num - k) * d[k] + d[k] * (d[k] - 1) // 2
            num += d[k]
        return move


if __name__ == '__main__':
    A = [3, 2, 1, 2, 1, 7]
    s = Solution()
    print(s.minIncrementForUnique4(A))
