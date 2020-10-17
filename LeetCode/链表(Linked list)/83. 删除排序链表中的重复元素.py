"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        while head:
            pre = head
            while head and head.val == pre.val:
                head = head.next
            pre.next = head
        return dummy.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next
