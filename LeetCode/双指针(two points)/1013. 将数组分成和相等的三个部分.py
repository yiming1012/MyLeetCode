"""
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1] 就可以将数组三等分。

 

示例 1：

输入：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
示例 2：

输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
示例 3：

输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

提示：

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        """
        思路：双指针
        1. 如果列表的总和不能被3整除，返回FALSE
        2. 如果列表总和能被3整除，分别从左右两端找到和为target的子序列即可
        @param A:
        @return:
        """
        S = sum(A)
        if S % 3 != 0:
            return False
        target = S // 3
        l, r = 0, len(A) - 1
        left, right = 0, 0

        while l < r:
            left += A[l]
            if left == target:
                break
            l += 1

        while l < r:
            right += A[r]
            if right == target:
                break
            r -= 1
        # print(l,r)
        if l + 1 < r and left == target and right == target:
            return True

        return False


if __name__ == '__main__':
    A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    print(Solution().canThreePartsEqualSum(A))
