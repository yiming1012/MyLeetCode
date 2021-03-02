"""
1054. 距离相等的条形码
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。

请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。



示例 1：

输入：[1,1,1,2,2,2]
输出：[2,1,2,1,2,1]
示例 2：

输入：[1,1,1,1,2,2,3,3]
输出：[1,3,1,3,2,1,2,1]


提示：

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
"""
from typing import List
import heapq
from collections import Counter




class Solution:
    def rearrangeBarcodes1(self, b: List[int]) -> List[int]:
        cnt = Counter[b]
        heap = []
        for k, v in cnt.items():
            heapq.heappush(heap, (-v, k))
        res = []
        while len(heap) > 1:
            v1, k1 = heapq.heappop(heap)
            v2, k2 = heapq.heappop(heap)
            res.extend([k1, k2])
            if v1 + 1 < 0:
                heapq.heappush(heap, (v1 + 1, k1))
            if v2 + 1 < 0:
                heapq.heappush(heap, (v2 + 1, k2))
        if heap:
            v, k = heapq.heappop(heap)
            res.append(k)
        return res

    def rearrangeBarcodes2(self, b: List[int]) -> List[int]:
        n = len(b)
        arr = [(k, v) for k, v in Counter(b).items()]
        arr.sort(key=lambda x: x[1], reverse=True)
        nums = []
        for k, v in arr:
            nums.extend([k] * v)
        res = [0] * n
        res[0:n:2] = nums[:(n + 1) // 2]
        res[1:n:2] = nums[(n + 1) // 2:]
        return res


if __name__ == '__main__':
    b = [1, 1, 1, 2, 2, 2]
    print(Solution().rearrangeBarcodes1(b))
    print(Solution().rearrangeBarcodes2(b))
