# Definition for singly-linked list.
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            nextNone = head.next
            head.next = pre
            pre = head
            head = nextNone
        return pre


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io


    line = "[1,2,3,4,5]"
    # while True:
    try:
        # line = next(lines)
        head = stringToListNode(line);
        ret = Solution().reverseList(head)
        out = listNodeToString(ret);
        print(out)
    except StopIteration:
        print(StopIteration)


if __name__ == '__main__':
    main()