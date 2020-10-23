"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        思路：双指针
        1. head表示原链表的当前节点，pre代表前一个节点的值，cur代表新链表的当前节点

        @param head:
        @return:
        """
        if not head:
            return
        dummy = ListNode(0)
        cur = dummy
        pre = None
        while head:
            # 如果当前节点与下一个节点值相同，指针向后移动
            while head.next and head.val == head.next.val:
                pre = head.val
                head = head.next
            # 此时当前节点和下一个节点值不相同，则判断当前值和前一个值是否相同，如果不同，说明当前节点需要添加到新链表中
            if head and head.val != pre:
                cur.next = head
                cur = cur.next
            head = head.next
        # 最后将新链表的最后指针的下一个位置指向空
        cur.next = None

        return dummy.next
