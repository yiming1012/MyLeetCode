"""
255. 验证前序遍历序列二叉搜索树
给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。

你可以假定该序列中的数都是不相同的。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [5,2,6,1,3]
输出: false
示例 2：

输入: [5,2,1,3,6]
输出: true
进阶挑战：

您能否使用恒定的空间复杂度来完成此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """
        思路：出栈的顺序就是中序遍历的顺序
        @param preorder:
        @return:
        """
        stack = []
        pre = float('-inf')
        for num in preorder:
            if pre > num: return False
            # 右子树
            while stack and stack[-1] < num:
                pre = stack.pop()
            stack.append(num)
        return True


if __name__ == '__main__':
    preorder = [5, 2, 6, 1, 3]
    print(Solution().verifyPreorder(preorder))
