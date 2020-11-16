"""
421. 数组中两个数的最大异或值
给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 231 。

找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i,  j < n 。

你能在O(n)的时间解决这个问题吗？

示例:

输入: [3, 10, 5, 25, 2, 8]

输出: 28

解释: 最大的结果是 5 ^ 25 = 28.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findMaximumXOR1(self, nums: List[int]) -> int:
        """
        思路：前缀树
        1. 先将每个数的二进制位从高到底插入前缀树
        2. 每个单词去前缀树中查找与当前二进制位不同的分支
        3. 每次记录最大值即可
        @param nums:
        @return:
        """
        trie = {}

        def insert(num):
            root = trie
            for i in range(30, -1, -1):
                u = num >> i & 1
                if u not in root:
                    root[u] = {}
                root = root[u]
            root["#"] = "#"

        def query(num):
            root = trie
            cnt = 0
            for i in range(30, -1, -1):
                u = num >> i & 1
                if 1 - u in root:
                    cnt = cnt * 2 + 1 - u
                    root = root[1 - u]
                else:
                    cnt = cnt * 2 + u
                    root = root[u]
            return cnt

        res = 0
        for num in nums:
            insert(num)
            t = query(num)
            res = max(res, num ^ t)
        return res

    def findMaximumXOR2(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        print(L)
        max_xor = 0
        for i in range(L)[::-1]:
            print(i)
            max_xor <<= 1

            curr_xor = max_xor | 1

            prefixes = {num >> i for num in nums}

            max_xor |= any(curr_xor ^ p in prefixes for p in prefixes)
        return max_xor


if __name__ == '__main__':
    nums = [3, 10, 5, 25, 2, 8]
    print(Solution().findMaximumXOR1(nums))
    print(Solution().findMaximumXOR2(nums))
