'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return False
        node = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1:
            node.next = l1
        if l2:
            node.next = l2

        return dummy.next


from ArrToLinkedList import ArrToLinkedList

if __name__ == '__main__':
    l1 = [1, 4, 7]
    l2 = [2, 4, 5, 6]
    # 调用函数将数组转换为链表
    obj=ArrToLinkedList()
    p = obj.arrToListNode(l1)
    q = obj.arrToListNode(l2)
    res = Solution().mergeTwoLists(p, q)
    while res:
        print(res.val)
        res = res.next
