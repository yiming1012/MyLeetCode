'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        执行用时 :136 ms, 在所有 Python3 提交中击败了41.59%的用户
        内存消耗 :16.6 MB, 在所有 Python3 提交中击败了21.43%的用户
        :param lists:
        :return:
        '''
        def merge(node1, node2):
            dummy = node = ListNode(0)
            while node1 and node2:
                if node1.val < node2.val:
                    node.next = node1
                    node1 = node1.next
                else:
                    node.next = node2
                    node2 = node2.next
                node = node.next

            if node1:
                node.next = node1

            if node2:
                node.next = node2

            return dummy.next

        length = len(lists)
        # 边界情况
        if length == 0:
            return None
        if length == 1:
            return lists[0]

        # 分治
        mid = length // 2
        return merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:length]))

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        '''
        执行用时 :100 ms, 在所有 Python3 提交中击败了71.39%的用户
        内存消耗 :17.5 MB, 在所有 Python3 提交中击败了7.14%的用户
        :param lists:
        :return:
        '''
        import heapq
        heap = []
        # heapq.heapify(heap)
        for list in lists:
            while list:
                heapq.heappush(heap, list.val)
                list = list.next
        dummy = node = ListNode(0)
        while heap:
            node.next = ListNode(heapq.heappop(heap))
            node = node.next
        return dummy.next
