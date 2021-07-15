"""
5790. 查询差绝对值的最小值
一个数组 a 的 差绝对值的最小值 定义为：0 <= i < j < a.length 且 a[i] != a[j] 的 |a[i] - a[j]| 的 最小值。如果 a 中所有元素都 相同 ，那么差绝对值的最小值为 -1 。

比方说，数组 [5,2,3,7,2] 差绝对值的最小值是 |2 - 3| = 1 。注意答案不为 0 ，因为 a[i] 和 a[j] 必须不相等。
给你一个整数数组 nums 和查询数组 queries ，其中 queries[i] = [li, ri] 。对于每个查询 i ，计算 子数组 nums[li...ri] 中 差绝对值的最小值 ，子数组 nums[li...ri] 包含 nums 数组（下标从 0 开始）中下标在 li 和 ri 之间的所有元素（包含 li 和 ri 在内）。

请你返回 ans 数组，其中 ans[i] 是第 i 个查询的答案。

子数组 是一个数组中连续的一段元素。

|x| 的值定义为：

如果 x >= 0 ，那么值为 x 。
如果 x < 0 ，那么值为 -x 。
 

示例 1：

输入：nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]
输出：[2,1,4,1]
解释：查询结果如下：
- queries[0] = [0,1]：子数组是 [1,3] ，差绝对值的最小值为 |1-3| = 2 。
- queries[1] = [1,2]：子数组是 [3,4] ，差绝对值的最小值为 |3-4| = 1 。
- queries[2] = [2,3]：子数组是 [4,8] ，差绝对值的最小值为 |4-8| = 4 。
- queries[3] = [0,3]：子数组是 [1,3,4,8] ，差的绝对值的最小值为 |3-4| = 1 。
示例 2：

输入：nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]
输出：[-1,1,1,3]
解释：查询结果如下：
- queries[0] = [2,3]：子数组是 [2,2] ，差绝对值的最小值为 -1 ，因为所有元素相等。
- queries[1] = [0,2]：子数组是 [4,5,2] ，差绝对值的最小值为 |4-5| = 1 。
- queries[2] = [0,5]：子数组是 [4,5,2,2,7,10] ，差绝对值的最小值为 |4-5| = 1 。
- queries[3] = [3,5]：子数组是 [2,7,10] ，差绝对值的最小值为 |7-10| = 3 。
 

提示：

2 <= nums.length <= 105
1 <= nums[i] <= 100
1 <= queries.length <= 2 * 104
0 <= li < ri < nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-difference-queries
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
import bisect
from cmath import inf
from typing import List


class Solution:
    def minDifference1(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        思路：前缀和
        @param nums:
        @param queries:
        @return:
        """
        n = len(nums)
        dp = [[0] * 101 for _ in range(n + 1)]
        for i in range(n):
            for j in range(1, 101):
                dp[i + 1][j] = dp[i][j]
                dp[i + 1][nums[i]] += 1

        res = [-1] * len(queries)
        for i, (l, r) in enumerate(queries):
            minv = inf
            pre = -inf

            for j in range(1, 101):
                if dp[r + 1][j] - dp[l][j] > 0:
                    minv = min(minv, j - pre)
                    pre = j

            if minv != inf:
                res[i] = minv

        return res

    def minDifference2(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 将每个数字对应的下标存入哈希表
        dic = collections.defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)

        res = [-1] * len(queries)
        # 查询
        for i, (l, r) in enumerate(queries):
            pre = -inf
            minv = inf
            # 遍历1~100中的数字是否存在于区间[l,r]中，相邻数之差最小
            for j in range(1, 101):
                a = bisect.bisect_left(dic[j], l)
                b = bisect.bisect_right(dic[j], r) - 1
                if a <= b:
                    minv = min(minv, j - pre)
                    pre = j
            # 区间内没有不相同的数据
            if minv != inf:
                res[i] = minv
        return res


if __name__ == '__main__':
    nums = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [2, 3], [0, 3]]
    print(Solution().minDifference1(nums, queries))
    print(Solution().minDifference2(nums, queries))