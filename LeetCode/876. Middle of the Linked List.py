'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.



Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.


Note:

The number of nodes in the given list will be between 1 and 100.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了54.54%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.55%的用户
        思路：定义两个快慢指针slow和fast。slow走一步，fast走两步，注意fast可能会走一步后就不能走了，需要break
        :param head:
        :return:
        '''
        slow = fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next

            if fast.next:
                fast = fast.next

        '''
        上面的while循环可以简化为下面的代码：
        '''
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    s = Solution()
    print(s.middleNode(A))
