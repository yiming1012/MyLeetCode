"""
659. 分割数组为连续子序列
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。

如果可以完成上述分割，则返回 true ；否则，返回 false 。

 

示例 1：

输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5
 

示例 2：

输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3, 4, 5
3, 4, 5
 

示例 3：

输入: [1,2,3,4,4,5]
输出: False
 

提示：

输入的数组长度范围为 [1, 10000]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections, heapq
from typing import List


class Solution:
    def isPossible1(self, nums: List[int]) -> bool:
        """
        思路：贪心算法
        1. 把短的或者或者重新开始的放在开头，可保证新来的元素放在短的后面
        @param nums:
        @return:
        """
        stack = []
        for num in nums:
            for i, arr in enumerate(stack):
                if arr and arr[-1] + 1 == num:
                    arr.append(num)
                    break
            else:
                stack.insert(0, [num])

        return min(map(len, stack)) >= 3

    def isPossible2(self, nums: List[int]) -> bool:
        """
        思路：哈希表存储以X结尾的序列的长度
        @param nums:
        @return:
        """
        mp = collections.defaultdict(list)
        for x in nums:
            if mp.get(x - 1):
                queue = mp.get(x - 1)
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)

        return not any(queue and queue[0] < 3 for queue in mp.values())


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 4, 5]
    print(Solution().isPossible1(nums))
    print(Solution().isPossible2(nums))
