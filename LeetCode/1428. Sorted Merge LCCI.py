'''
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.

Initially the number of elements in A and B are m and n respectively.

Example:

Input:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

'''
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        执行用时 :36 ms, 在所有 Python3 提交中击败了89.15%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了100.00%的用户
        Do not return anything, modify A in-place instead.
        """
        while m > 0 and n > 0:
            if A[m - 1] > B[n - 1]:
                A[m + n - 1] = A[m - 1]
                m -= 1
            else:
                A[m + n - 1] = B[n - 1]
                n -= 1
        # 如果B没有结束，将B中元素放到A中对应的位置
        while n > 0:
            A[n - 1] = B[n - 1]
            n -= 1
        return A

    def merge2(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        执行用时 :44 ms, 在所有 Python3 提交中击败了50.39%的用户
        内存消耗 :13.3 MB, 在所有 Python3 提交中击败了100.00%的用户
        Do not return anything, modify A in-place instead.
        """
        A[m:m + n] = B
        return A.sort()
'''
1、逆序
'''

s = Solution()
A = [1, 2, 3, 0, 0, 0, 0]
m = 3
B = [2, 5, 6]
n = 3
print(s.merge(A, m, B, n))
