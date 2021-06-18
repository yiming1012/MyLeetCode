"""
952. 按公因数计算最大组件大小
给定一个由不同正整数的组成的非空数组 A，考虑下面的图：

有 A.length 个节点，按从 A[0] 到 A[A.length - 1] 标记；
只有当 A[i] 和 A[j] 共用一个大于 1 的公因数时，A[i] 和 A[j] 之间才有一条边。
返回图中最大连通组件的大小。

 

示例 1：

输入：[4,6,15,35]
输出：4

示例 2：

输入：[20,50,9,63]
输出：2

示例 3：

输入：[2,3,6,7,4,12,21,39]
输出：8

 

提示：

1 <= A.length <= 20000
1 <= A[i] <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-component-size-by-common-factor
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        N = 10 ** 5 + 10
        # 并查集模板
        parent = list(range(N))

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                parent[b] = a

        # 分解因子，求连通块
        for num in nums:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    union(num, i)
                    if num // i != i:
                        union(num, num // i)

        cnt = collections.defaultdict(lambda: 0)
        res = 0
        # 计算每个根节点对应的连通区域大小
        for num in nums:
            root = find(num)
            cnt[root] += 1
            res = max(res, cnt[root])
        return res


if __name__ == '__main__':
    nums=[4, 6, 15, 35]
    print(Solution().largestComponentSize(nums))





