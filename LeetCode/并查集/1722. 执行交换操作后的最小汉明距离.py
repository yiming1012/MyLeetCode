"""
1722. 执行交换操作后的最小汉明距离
给你两个整数数组 source 和 target ，长度都是 n 。还有一个数组 allowedSwaps ，其中每个 allowedSwaps[i] = [ai, bi] 表示你可以交换数组 source 中下标为 ai 和 bi（下标从 0 开始）的两个元素。注意，你可以按 任意 顺序 多次 交换一对特定下标指向的元素。

相同长度的两个数组 source 和 target 间的 汉明距离 是元素不同的下标数量。形式上，其值等于满足 source[i] != target[i] （下标从 0 开始）的下标 i（0 <= i <= n-1）的数量。

在对数组 source 执行 任意 数量的交换操作后，返回 source 和 target 间的 最小汉明距离 。

 

示例 1：

输入：source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
输出：1
解释：source 可以按下述方式转换：
- 交换下标 0 和 1 指向的元素：source = [2,1,3,4]
- 交换下标 2 和 3 指向的元素：source = [2,1,4,3]
source 和 target 间的汉明距离是 1 ，二者有 1 处元素不同，在下标 3 。
示例 2：

输入：source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
输出：2
解释：不能对 source 执行交换操作。
source 和 target 间的汉明距离是 2 ，二者有 2 处元素不同，在下标 1 和下标 2 。
示例 3：

输入：source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
输出：0
 

提示：

n == source.length == target.length
1 <= n <= 105
1 <= source[i], target[i] <= 105
0 <= allowedSwaps.length <= 105
allowedSwaps[i].length == 2
0 <= ai, bi <= n - 1
ai != bi

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimize-hamming-distance-after-swap-operations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict, Counter
from typing import List


class DSU:
    def __init__(self, n):
        self.uf = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        ans = False
        if px != py:
            if self.rank[px] > self.rank[py]:
                px, py = py, px
            self.rank[py] += self.rank[px]
            self.uf[px] = py
            ans = True
        return ans


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        dsu = DSU(n)
        for a, b in allowedSwaps:
            dsu.union(a, b)
        dic = defaultdict(list)
        for i in range(n):
            dic[dsu.find(i)].append(i)
        ans = 0
        for v in dic.values():
            cnt1, cnt2 = Counter(), Counter()
            for i in v:
                cnt1[source[i]] += 1
                cnt2[target[i]] += 1
            cur = list((cnt1 & cnt2).elements())
            ans += len(cur)
        return n - ans


if __name__ == '__main__':
    source = [1, 2, 3, 4]
    target = [2, 1, 4, 5]
    allowedSwaps = [[0, 1], [2, 3]]
    print(Solution().minimumHammingDistance(source, target, allowedSwaps))
