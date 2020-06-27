"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:

 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
示例2:

 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]
提示：

链表长度在[0, 20000]范围内。
链表元素在[0, 20000]范围内。
进阶：

如果不得使用临时缓冲区，该怎么解决？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes1(self, head: ListNode) -> ListNode:
        """
        思路：每次判断node.next
        """
        dic = set()
        dummy = node = ListNode(0)
        node.next = head
        while node.next:
            if node.next.val in dic:
                node.next = node.next.next
            else:
                dic.add(node.next.val)
                node = node.next
        return dummy.next

    def removeDuplicateNodes2(self, head):
        """
        更快的
        """
        d = set()
        hh = head
        bf = ''
        while head:
            if head.val not in d:
                d.add(head.val)
                bf = head
            else:
                bf.next = head.next
            head = head.next
        return hh