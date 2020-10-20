"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        思路：
        1. 利用数组将链表节点存储后逆序匹配即可
        2. 最后遍历到的节点的下一个指针需指向空
        @param head:
        @return:
        """
        if not head:
            return
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        n = len(arr)
        now = head
        i = 0
        while i < n // 2:
            nex = now.next
            now.next = arr[n - i - 1]
            now.next.next = nex
            now = nex
            i += 1
        now.next = None