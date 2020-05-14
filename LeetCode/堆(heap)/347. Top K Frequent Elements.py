'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了97.28%的用户
        内存消耗 :16.5 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param nums:
        :param k:
        :return:
        '''
        return [tp[0] for tp in collections.Counter(nums).most_common(k)]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了97.28%的用户
        内存消耗 :16.5 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param nums:
        :param k:
        :return:
        '''
        import heapq
        c = collections.Counter(nums)
        return heapq.nlargest(k, c, key=lambda x: c[x])

    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        # return [tp[0] for tp in collections.Counter(nums).most_common(k)]
        dic = collections.Counter(nums)
        print(dic)
        res = []
        for key, value in dic.items():
            heapq.heappush(res, [-value, key])

        arr = []
        for _ in range(k):
            p = heapq.heappop(res)
            arr.append(p[1])
        return arr


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent2(nums, k))
