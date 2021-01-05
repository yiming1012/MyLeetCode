"""
1273. 删除树节点
给你一棵以节点 0 为根节点的树，定义如下：

节点的总数为 nodes 个；
第 i 个节点的值为 value[i] ；
第 i 个节点的父节点是 parent[i] 。
请你删除节点值之和为 0 的每一棵子树。

在完成所有删除之后，返回树中剩余节点的数目。



示例 1：



输入：nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
输出：2
示例 2：

输入：nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
输出：6
示例 3：

输入：nodes = 5, parent = [-1,0,1,0,0], value = [-672,441,18,728,378]
输出：5
示例 4：

输入：nodes = 5, parent = [-1,0,0,1,1], value = [-686,-842,616,-739,-746]
输出：5


提示：

1 <= nodes <= 10^4
parent.length == nodes
0 <= parent[i] <= nodes - 1
parent[0] == -1 表示节点 0 是树的根。
value.length == nodes
-10^5 <= value[i] <= 10^5
题目输入数据 保证 是一棵 有效的树 。
"""
import collections
from typing import List


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        # 构建树
        graph = collections.defaultdict(list)
        for i, num in enumerate(parent):
            graph[num].append(i)

        value1 = [-1] * nodes

        # 计算以每个节点为根节点的子树的节点值之和，用value1存储
        def dfs(root):
            ans = value[root]
            for nex in graph[root]:
                ans += dfs(nex)
            value1[root] = ans
            return ans

        dfs(0)
        res = 0

        # 从根节点遍历，计算不为0的节点数，遇到0返回
        def count(root):
            if value1[root] == 0:
                return
            nonlocal res
            res += 1
            for nex in graph[root]:
                count(nex)

        count(0)
        return res


if __name__ == '__main__':
    nodes = 7
    parent = [-1, 0, 0, 1, 2, 2, 2]
    value = [1, -2, 4, 0, -2, -1, -1]
    print(Solution().deleteTreeNodes(nodes, parent, value))
