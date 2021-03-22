"""
1803. 统计异或值在范围内的数对有多少
给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数：low 和 high ，请返回 漂亮数对 的数目。

漂亮数对 是一个形如 (i, j) 的数对，其中 0 <= i < j < nums.length 且 low <= (nums[i] XOR nums[j]) <= high 。

 

示例 1：

输入：nums = [1,4,2,7], low = 2, high = 6
输出：6
解释：所有漂亮数对 (i, j) 列出如下：
    - (0, 1): nums[0] XOR nums[1] = 5
    - (0, 2): nums[0] XOR nums[2] = 3
    - (0, 3): nums[0] XOR nums[3] = 6
    - (1, 2): nums[1] XOR nums[2] = 6
    - (1, 3): nums[1] XOR nums[3] = 3
    - (2, 3): nums[2] XOR nums[3] = 5
示例 2：

输入：nums = [9,8,4,2,1], low = 5, high = 14
输出：8
解释：所有漂亮数对 (i, j) 列出如下：
​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
    - (0, 3): nums[0] XOR nums[3] = 11
    - (0, 4): nums[0] XOR nums[4] = 8
    - (1, 2): nums[1] XOR nums[2] = 12
    - (1, 3): nums[1] XOR nums[3] = 10
    - (1, 4): nums[1] XOR nums[4] = 9
    - (2, 3): nums[2] XOR nums[3] = 6
    - (2, 4): nums[2] XOR nums[4] = 5
 

提示：

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 2 * 104
1 <= low <= high <= 2 * 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-pairs-with-xor-in-a-range
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        class TrieNode:

            def __init__(self):
                self.child = [None, None]
                self.cnt = 0

        ROOT = TrieNode()

        def insert(root, N):
            for i in range(15, -1, -1):
                ind = N >> i & 1
                if not root.child[ind]:
                    root.child[ind] = TrieNode()
                root.child[ind].cnt += 1
                root = root.child[ind]

        def count_small(root, N, K):
            print(N, K)
            res = 0
            for i in range(15, -1, -1):
                if not root:
                    break
                x = N >> i & 1
                y = K >> i & 1
                print(N, K, x, y)
                if y == 1:
                    if root.child[x]:
                        res += root.child[x].cnt
                    root = root.child[1 - x]
                else:
                    root = root.child[x]
            return res

        ans = 0
        for i in nums:
            ans += (count_small(ROOT, i, high + 1) - count_small(ROOT, i, low))
            insert(ROOT, i)

        return ans


if __name__ == '__main__':
    nums = [1, 4, 2, 7]
    low = 2
    high = 6
    print(Solution().countPairs(nums, low, high))
