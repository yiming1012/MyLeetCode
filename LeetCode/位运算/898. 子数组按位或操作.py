"""

输入：[1,2,4]
输出：6
解释：
可能的结果是 1，2，3，4，6，以及 7 。
 

提示：

1 <= A.length <= 50000
0 <= A[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bitwise-ors-of-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        """
        # 利用集合set的性质，意义不大
        @param A:
        @return:
        """

        cur = set()
        res = set()
        for num in A:
            cur = {num | i for i in cur} | {num}
            res |= cur
        return len(res)


if __name__ == '__main__':
    A = [1, 2, 4]
    print(Solution().subarrayBitwiseORs(A))
