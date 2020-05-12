class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ArrToLinkedList:
    def arrToListNode(self, numbers):
        # Now convert that list into linked list
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in numbers:
            ptr.next = ListNode(number)
            ptr = ptr.next

        ptr = dummyRoot.next
        return ptr

if __name__ == '__main__':
    numbers=[1,2,3]
    print(ArrToLinkedList().arrToListNode(numbers))