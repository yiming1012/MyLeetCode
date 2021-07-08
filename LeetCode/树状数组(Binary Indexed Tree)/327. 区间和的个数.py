"""
327. 区间和的个数
给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 区间和的个数 。

区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

 

示例 1：
输入：nums = [-2,5,-1], lower = -2, upper = 2
输出：3
解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。
示例 2：

输入：nums = [0], lower = 0, upper = 0
输出：1
 

提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
-105 <= lower <= upper <= 105
题目数据保证答案是一个 32 位 的整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-range-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def lowbit(x):
            return x & -x

        def query(x):
            res = 0
            while x > 0:
                res += base[x]
                x -= lowbit(x)
            return res

        def update(x):
            while x <= len(rank):
                base[x] += 1
                x += lowbit(x)

        n = len(nums)
        pre = [0] * (n + 1)
        # 前缀和
        for i, num in enumerate(nums):
            pre[i + 1] = pre[i] + num
        # pre = [0, *itertools.accumulate(nums)]

        # 离散化(将其转换为1-n个连续的点)
        rank = {}
        treeval = []
        for p in pre:
            treeval.extend([p - lower, p, p - upper])

        treeval = sorted(set(treeval))

        x = 1
        for i in treeval:
            rank[i] = x
            x += 1

        # 树节点数组
        base = [0] * (1 + len(rank))
        res = 0
        # 区间检索
        for i in range(n + 1):
            left, right = pre[i] - upper, pre[i] - lower
            res += query(rank[right]) - query(rank[left] - 1)
            print(i, res)
            update(rank[pre[i]])
        return res