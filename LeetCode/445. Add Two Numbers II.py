'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    注意：这里有一个知名的错误：Python整数相加，不会溢出，所以不能这么做
    '''

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        执行用时 :80 ms, 在所有 Python3 提交中击败了68.00%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了50.00%的用户
        思路：1、先将两个链表转换为整数，相加得sum
        2、利用一个指针指向sum，注意每一位为为ListNode(int(i))

        :param l1:
        :param l2:
        :return:
        '''
        num1 = l1.val
        num2 = l2.val
        while l1.next:
            l1 = l1.next
            num1 = num1 * 10 + l1.val
        while l2.next:
            l2 = l2.next
            num2 = num2 * 10 + l2.val

        num = str(num1 + num2)
        # print(num)

        dummy = node = ListNode(0)
        for i in num:
            node.next = ListNode(int(i))
            node = node.next

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        执行用时 :148 ms, 在所有 Python3 提交中击败了5.72%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了50.00%的用户
        思路：由于不能直接将两个数相加，所以只能通过指针相加
        1、将每个数，加入到stack中
        2、将stack中的尾部数据pop出来num，令sum=carry（上一步是否有进位），sum+num1+num2
        3、因为尾部数据是逆序的，所以需要采用链表头插法来完成
            node=ListNode(sum%10)
            node.next=dummy.next
            dummy.next=node

        :param l1:
        :param l2:
        :return:
        '''
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        # print(stack1)
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        # print(stack2)

        carry = 0
        dummy = ListNode(0)
        while stack1 or stack2 or carry > 0:
            sum = carry
            sum += stack1.pop() if stack1 else 0
            sum += stack2.pop() if stack2 else 0
            node = ListNode(sum % 10)
            node.next = dummy.next
            dummy.next = node
            carry = sum // 10
        return dummy.next


if __name__ == '__main__':
    l1 = [2, 4, 3, 5]
    l2 = [3, 4, 5]
    s = Solution()
    print(s.addTwoNumbers(l1, l2))
