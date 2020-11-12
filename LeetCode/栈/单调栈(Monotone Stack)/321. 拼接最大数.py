"""
321. 拼接最大数
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
示例 2:

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
示例 3:

输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/create-maximum-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # 合并两相对位置不变数组
        def merge(A, B):
            stack = []
            while A or B:
                if A > B:
                    stack.append(A.pop(0))
                else:
                    stack.append(B.pop(0))
            return stack

        # 获取A数组中长度为length的最大字典序
        def kMax(A, length):
            stack = []
            rest = len(A) - length
            for i, c in enumerate(A):
                while stack and stack[-1] < c and rest > 0:
                    stack.pop()
                    rest -= 1
                stack.append(c)
            return stack[:-rest] if rest > 0 else stack

        # 遍历nums1和nums2可组合成长度为k的序列每一种情况
        res = []
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                a = kMax(nums1, i)
                b = kMax(nums2, k - i)
                res = max(res, merge(a, b))
        return res


if __name__ == '__main__':
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    print(Solution().maxNumber(nums1, nums2, k))
