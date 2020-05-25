"""
在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。



给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。

 

示例 1：

输入：label = 14
输出：[1,3,4,14]
示例 2：

输入：label = 26
输出：[1,2,6,10,26]
 

提示：

1 <= label <= 10^6


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 获取layer
        layer = 0
        num = label
        while num:
            num >>= 1
            layer += 1
        arr = [label]
        for i in range(layer - 1, 0, -1):
            label = 3 * (2 ** (i - 1)) - 1 - label // 2
            arr.insert(0, label)
        return arr

    def pathInZigZagTree2(self, label: int) -> List[int]:
        res = []
        while label != 1:
            res.append(label)
            label >>= 1
            # 这里我采用异或实现
            label = label ^ (1 << (label.bit_length() - 1)) - 1
        return [1] + res[::-1]
