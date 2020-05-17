class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListToArr:
    def listNodeToArr(self, node):
        # Now convert that list into linked list
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        return arr


if __name__ == '__main__':
    head = ListNode(1)
    head.next=ListNode(2)
    print(LinkedListToArr().listNodeToArr(head))
