'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了81.39%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.41%的用户
        :param head:
        :param n:
        :return:
        '''
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        node = head
        while n > 0 and node:
            n -= 1
            node = node.next
        if n > 0:
            return None
        if n == 0 and not node:
            dummy.next = head.next
            return dummy.next
        while node.next:
            head = head.next
            node = node.next
        head.next = head.next.next
        return dummy.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        '''
        执行用时 :48 ms, 在所有 Python3 提交中击败了31.34%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.41%的用户
        思路：1、设置一个dummy Node，下一位指向head，因为head有可能被删掉
        :param head:
        :param n:
        :return:
        '''
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        while n > 0 and fast.next:
            fast = fast.next
            n -= 1

        # if n>0:
        #     return dummy.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next