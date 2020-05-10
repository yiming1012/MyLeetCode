"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        时间复杂度：一般情况下是 O(m+n)O(m+n)，最坏情况下是 O(m \times n)O(m×n)。
        空间复杂度：最坏的情况是 O(m+n)O(m+n)，当数组中的元素全部不一样时。
        set的去重是通过两个函数__hash__和__eq__结合实现的。
        1、当两个变量的哈希值不相同时，就认为这两个变量是不同的
        2、当两个变量哈希值一样时，调用__eq__方法，当返回值为True时认为这两个变量是同一个，应该去除一个。返回FALSE时，不去重

        """
        #return [i for i in list(set(nums1)) if i in list(set(nums2))]
        return list(set(nums1)&set(nums2))
