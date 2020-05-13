class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ArrToLinkedList:
    def arrToListNode(self, numbers):
        # Now convert that list into linked list
        dummy = ListNode(0)
        ptr = dummy
        for number in numbers:
            ptr.next = ListNode(number)
            ptr = ptr.next

        ptr = dummy.next
        return ptr


if __name__ == '__main__':
    arr = [1, 2, 3]
    res = ArrToLinkedList().arrToListNode(arr)
    while res:
        print(res.val)
        res = res.next
