"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        """
        本题和905题类似，思路双指针
        这种题都要注意边界的判断，防止下标溢出
        时间复杂度：O(N)
        空间复杂度：O(1)
        """
        n = len(A)
        left, right = 0, n - 1
        while left < n and right >= 0:
            while left < n and A[left] & 1 == 0:
                left += 2
            while right >= 0 and A[right] & 1 == 1:
                right -= 2
            if left < n and right >= 0:
                A[left], A[right] = A[right], A[left]
        return A
