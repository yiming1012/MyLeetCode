"""
给定一个数组 A，将其划分为两个不相交（没有公共元素）的连续子数组 left 和 right， 使得：

left 中的每个元素都小于或等于 right 中的每个元素。
left 和 right 都是非空的。
left 要尽可能小。
在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。

 

示例 1：

输入：[5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]
示例 2：

输入：[1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]
 

提示：

2 <= A.length <= 30000
0 <= A[i] <= 10^6
可以保证至少有一种方法能够按题目所描述的那样对 A 进行划分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-array-into-disjoint-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        """
        思路：
        1. 从左到右，记录当前的最大值；从右到左，记录当前的最小值；
        2. 遍历找到第一个左边的最大值不大于右边最小值的index
        """
        n = len(A)
        preMax = [A[0]] * n
        nexMin = [A[n - 1]] * n

        for i in range(1, n):
            preMax[i] = max(preMax[i - 1], A[i])
            nexMin[n - i - 1] = min(nexMin[n - i], A[n - i - 1])

        for i in range(n - 1):
            if preMax[i] <= nexMin[i + 1]:
                return i + 1

    def partitionDisjoint2(self, A: List[int]) -> int:
        """
        思路：
        1. 每次记录截止当前的最大值，当出现一个值小于当前最大值时，记录当前index
        2. 如果后面的子序列都比当前最大值大，则不会更新index
        """
        n = len(A)
        index = 0
        cur = leftMax = A[0]
        for i in range(n):
            leftMax = max(leftMax, A[i])
            if A[i] < cur:
                cur = leftMax
                index = i
        return index + 1

    def partitionDisjoint3(self, A: 'List[int]') -> 'int':
        lmaxv = A[0]
        maxv = A[0]
        l = 0

        for i in range(len(A)):
            if A[i] < lmaxv:
                lmaxv = maxv
                l = i
            if A[i] > maxv:
                maxv = A[i]

        return l + 1


if __name__ == '__main__':
    A = [5, 0, 3, 8, 6]
    print(Solution().partitionDisjoint(A))
    print(Solution().partitionDisjoint2(A))
