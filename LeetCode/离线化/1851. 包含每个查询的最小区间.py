"""
1851. 包含每个查询的最小区间
给你一个二维整数数组 intervals ，其中 intervals[i] = [lefti, righti] 表示第 i 个区间开始于 lefti 、结束于 righti（包含两侧取值，闭区间）。区间的 长度 定义为区间中包含的整数数目，更正式地表达是 righti - lefti + 1 。

再给你一个整数数组 queries 。第 j 个查询的答案是满足 lefti <= queries[j] <= righti 的 长度最小区间 i 的长度 。如果不存在这样的区间，那么答案是 -1 。

以数组形式返回对应查询的所有答案。

 

示例 1：

输入：intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
输出：[3,3,1,4]
解释：查询处理如下：
- Query = 2 ：区间 [2,4] 是包含 2 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 3 ：区间 [2,4] 是包含 3 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 4 ：区间 [4,4] 是包含 4 的最小区间，答案为 4 - 4 + 1 = 1 。
- Query = 5 ：区间 [3,6] 是包含 5 的最小区间，答案为 6 - 3 + 1 = 4 。
示例 2：

输入：intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
输出：[2,-1,4,6]
解释：查询处理如下：
- Query = 2 ：区间 [2,3] 是包含 2 的最小区间，答案为 3 - 2 + 1 = 2 。
- Query = 19：不存在包含 19 的区间，答案为 -1 。
- Query = 5 ：区间 [2,5] 是包含 5 的最小区间，答案为 5 - 2 + 1 = 4 。
- Query = 22：区间 [20,25] 是包含 22 的最小区间，答案为 25 - 20 + 1 = 6 。
 

提示：

1 <= intervals.length <= 105
1 <= queries.length <= 105
queries[i].length == 2
1 <= lefti <= righti <= 107
1 <= queries[j] <= 107

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-interval-to-include-each-query
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        思路：离线化，将查询数组和事物数组排序，降低时间复杂度（写了题解）
        @param rooms:
        @param queries:
        @return:
        """
        # 数组大小
        m, n = len(intervals), len(queries)
        # 返回值
        res = [-1] * n
        # 堆
        heap = []
        # 将queries中数字按照从小到大的顺序排列，并记录每个值对应的下标
        qr = sorted([(i, q) for i, q in enumerate(queries)], key=lambda x: x[1])
        # 将区间intervals排序
        intervals.sort()
        index = 0
        for i, q in qr:
            # 如果intervals中区间的左端点小于等于查询值q，则将区间的长度和右端点加入堆中
            while index < m and intervals[index][0] <= q:
                l, r = intervals[index]
                heapq.heappush(heap, [r - l + 1, r])
                index += 1
            # 如果堆顶元素存储的右端点小于查询值，则对顶元素出堆
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            # 如果堆不为空，堆顶元素即为所求
            if heap:
                res[i] = heap[0][0]
        return res
