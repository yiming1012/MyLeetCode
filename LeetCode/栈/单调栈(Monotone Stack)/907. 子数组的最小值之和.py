"""
给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。

由于答案可能很大，因此返回答案模 10^9 + 7。

 

示例：

输入：[3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
 

提示：

1 <= A <= 30000
1 <= A[i] <= 30000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-subarray-minimums
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        """
        思路：单调栈
        1. 利用单调栈保存单调递增的数据
        2. 当遇到一个比栈顶元素更小的数时，判断栈顶元素前后的距离left和right，包含栈顶元素且以其为最小值的子序列的个数个left*right
        3. 累加A[left]*left*right
        """
        res = 0
        A.append(0)
        stack = [-1]
        for i, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                left = stack.pop()
                res += (i - left) * A[left] * (left - stack[-1])
            stack.append(i)
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    A = [3, 1, 2, 4]
    print(Solution().sumSubarrayMins(A))
