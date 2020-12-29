"""
1361. 验证二叉树
二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。

只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。

如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。

注意：节点没有值，本问题中仅仅使用节点编号。

 

示例 1：



输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
输出：true
示例 2：



输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
输出：false
示例 3：



输入：n = 2, leftChild = [1,0], rightChild = [-1,-1]
输出：false
示例 4：



输入：n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
输出：false
 

提示：

1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-tree-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        # 判断节点入度
        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1
        root = None
        # 寻找根节点
        for i in range(n):
            if indegree[i] == 0:
                root = i
                break
        if root is None:
            return False
        visit = set()
        queue = collections.deque([root])
        # 遍历树
        while queue:
            i = queue.popleft()
            if i in visit:
                return False
            if leftChild[i] != -1:
                queue.append(leftChild[i])
            if rightChild[i] != -1:
                queue.append(rightChild[i])
            visit.add(i)
        return len(visit) == n


if __name__ == '__main__':
    n = 4
    leftChild = [1, -1, 3, -1]
    rightChild = [2, -1, -1, -1]
    print(Solution().validateBinaryTreeNodes(n, leftChild, rightChild))
