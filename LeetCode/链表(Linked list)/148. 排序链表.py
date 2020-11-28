"""
148. 排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
 

示例 1：


输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：


输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def sort(slow, fast):
            dummy = ListNode(0)
            node = dummy
            while slow and fast:
                if slow.val < fast.val:
                    node.next = slow
                    slow = slow.next
                else:
                    node.next = fast
                    fast = fast.next
                node = node.next

            if slow:
                node.next = slow
            if fast:
                node.next = fast
            return dummy.next

        def merge(head):
            if not head or not head.next:
                return head
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            fast = slow.next
            slow.next = None
            left = merge(head)
            right = merge(fast)
            return sort(left, right)

        return merge(head)
