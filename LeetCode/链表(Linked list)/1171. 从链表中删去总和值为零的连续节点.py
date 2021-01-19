"""
1171. 从链表中删去总和值为零的连续节点
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。

删除完毕后，请你返回最终结果链表的头节点。



你可以返回任何满足题目要求的答案。

（注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）

示例 1：

输入：head = [1,2,-3,3,1]
输出：[3,1]
提示：答案 [1,2,1] 也是正确的。
示例 2：

输入：head = [1,2,3,-3,4]
输出：[1,2,4]
示例 3：

输入：head = [1,2,3,-3,-2]
输出：[1]


提示：

给你的链表中可能有 1 到 1000 个节点。
对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        pre = 0
        visited = set([0])
        arr = []
        while head:
            arr.append(head.val)
            pre += head.val
            tmp = pre
            if pre in visited:
                while True:
                    visited.remove(pre)
                    num = arr.pop()
                    pre -= num
                    if pre == tmp:
                        break
            visited.add(tmp)
            head = head.next
        dummy = ListNode(0)
        head = dummy
        for a in arr:
            head.next = ListNode(a)
            head = head.next
        return dummy.next


    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        # 总和值为 0 的连续节点组成的序列
        dummy = ListNode(0)
        dummy.next = head
        d = dummy
        hp = {}
        cur_sum = 0
        # 第一次遍历
        while d:
            cur_sum += d.val
            hp[cur_sum] = d  # 覆盖更新为最新的位置
            d = d.next

        # 第二次遍历
        d = dummy
        cur_sum = 0
        while d:
            cur_sum += d.val
            d.next = hp.get(cur_sum).next
            d = d.next
        return dummy.next
