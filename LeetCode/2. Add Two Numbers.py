# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1.next)
        print(l2.next)
        return


if __name__ == '__main__':
    a = Solution()
    a.addTwoNumbers(2, 3)
