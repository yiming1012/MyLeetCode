# Definition for singly-linked list.
from ArrToLinkedList import ArrToLinkedList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = result = ListNode(0)
        flag = 0
        while l1 or l2 or flag:
            two_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + flag
            flag, mod = divmod(two_sum, 10)
            result.next = ListNode(mod)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            result = result.next

        return dummy.next


if __name__ == '__main__':
    # 将数组转换为链表
    a = ArrToLinkedList().arrToListNode([1, 2, 3])
    b = ArrToLinkedList().arrToListNode([4, 5, 6])
    res = Solution().addTwoNumbers(a, b)
    while res:
        print(res.val)
        res = res.next
