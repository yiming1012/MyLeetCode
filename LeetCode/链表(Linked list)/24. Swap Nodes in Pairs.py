"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ArrToLinkedList import ArrToLinkedList
from LinkedListToArr import LinkedListToArr


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = pre = ListNode(0)
        pre.next = head
        cur = head
        while cur and cur.next:
            # copy
            first = cur
            second = cur.next
            # 交换节点
            first.next = second.next
            second.next = first
            # 为下一轮做准备
            pre.next = second
            pre = first
            cur = pre.next

        return dummy.next

    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head

        while cur and cur.next:
            nex = cur.next
            pre.next = nex
            cur.next = nex.next
            nex.next = cur

            pre = cur
            cur = cur.next

        return dummy.next

    def swapPairs3(self, head: ListNode) -> ListNode:
        """
        思路：递归
        @param head:
        @return:
        """
        if not head or not head.next:
            return head
        nex = head.next
        head.next = self.swapPairs3(nex.next)
        nex.next = head
        return nex


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    # 数组转换为链表
    head = ArrToLinkedList().arrToListNode(arr)
    # node = Solution().swapPairs1(head)
    # node = Solution().swapPairs2(head)
    node = Solution().swapPairs3(head)
    # 链表转换为数组
    print(LinkedListToArr().listNodeToArr(node))
