"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        执行用时 :100 ms, 在所有 Python3 提交中击败了56.05%的用户
        内存消耗 :14.1 MB, 在所有 Python3 提交中击败了33.33%的用户
        思路：双指针（参考快排）
        1. 当前面的数为偶数时，left+=1，同时必须保证不能越界，即left<right
        2. 同理，后面的数为奇数时也是一样
        3. 最后，交换两个数的位置

        """
        n = len(A)
        left, right = 0, n - 1
        while left < right:
            while left < right and A[left] & 1 == 0:
                left += 1
            while left < right and A[right] & 1 == 1:
                right -= 1
            A[left], A[right] = A[right], A[left]
        return A

    def sortArrayByParity2(self, A: List[int]) -> List[int]:
        """
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        return [a for a in A if not a & 1] + [a for a in A if a & 1]
        # odd,even=[],[]
        # for a in A:
        #     if a&1:
        #         odd.append(a)
        #     else:
        #         even.append(a)
        # return even+odd

    def sortArrayByParity3(self, A):
        """
        时间复杂度：O(NlogN)
        空间复杂度：O(n)
        """
        A.sort(key=lambda x: x % 2)
        return A



if __name__ == '__main__':
    A=[2,3,2,1,5]
    print(Solution().sortArrayByParity2(A))