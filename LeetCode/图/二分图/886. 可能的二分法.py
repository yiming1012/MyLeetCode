"""
886. 可能的二分法
给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。

每个人都可能不喜欢其他人，那么他们不应该属于同一组。

形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。

当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。

 

示例 1：

输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]
示例 2：

输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false
示例 3：

输入：N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
输出：false
 

提示：

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
对于 dislikes[i] == dislikes[j] 不存在 i != j

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/possible-bipartition
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        """
        思路：dfs
        1. 染色法，记录遍历过的和未遍历过的对比
        @param N: 
        @param dislikes:
        @return:
        """
        # 染色法
        color = {}
        graph = collections.defaultdict(set)
        for u, v in dislikes:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(root, c):
            if root in color:
                return color[root] == c
            color[root] = c

            for nex in graph[root]:
                if not dfs(nex, c ^ 1):
                    return False
            return True

        for k in graph.keys():
            if k not in color and not dfs(k, 1):
                return False

        return True


if __name__ == '__main__':
    N = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    print(Solution().possibleBipartition(N, dislikes))
