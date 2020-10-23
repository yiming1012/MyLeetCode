"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        slow, fast = head, head
        # 寻找中点
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow.val)

        # 翻转后面链表
        pre = None
        nex = cur = slow
        while nex:
            nex = nex.next
            cur.next = pre
            pre = cur
            if nex:
                cur = nex

        # print(slow.val,cur.val)
        left = head
        # 头尾遍历
        while cur and left:
            if cur.val != left.val:
                return False
            left = left.next
            cur = cur.next

        return True
