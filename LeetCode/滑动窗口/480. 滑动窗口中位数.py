"""
480. 滑动窗口中位数
中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

例如：

[2,3,4]，中位数是 3
[2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

 

示例：

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。

 

提示：

你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-median
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import bisect
from typing import List

"""
解法二：数组+二分查找
维护一个数组 a，它保存当前数组，最开始等于排好序的 nums 的前 k 个元素。注意：a 是排好序的。
用 res 保存返回结果，首先将a加入。
用 i, j 循环 nums，它们分别表示删除值和加入值，每一对 i, j 都要执行下面步骤：
将 a 中值为 i 的元素删除；
将 j 增加在合适的位置，使用二分查找库（bisect）；
得到中位数并增加到 res 的最后。
返回。
举例
输入：nums = [1, 3, -1, -3, 5], k = 2
步骤：

a = [1, 3]，res = [a的中位数] = [2]
a = [1, 3]，删除1，增加-1，a = [-1, 3]，res增加a的中位数 = 1，res = [2, 1]
a = [-1, 3]，删除3，增加-3，a = [-3, -1]，res增加a的中位数 = -2，res = [2, 1, -2]
a = [-3, -1]，删除-1，增加5，a = [-3, 5]，res增加a的中位数 = 1，res = [2, 1, -2, 1]
返回res

"""


class Solution:
    def medianSlidingWindow1(self, nums: List[int], k: int) -> List[float]:
        """
        滑动窗口用zip真方便
        @param nums:
        @param k:
        @return:
        """
        median = lambda a: (a[(k - 1) // 2] + a[k // 2]) / 2
        a = sorted(nums[:k])
        res = [median(a)]
        for i, j in zip(nums[:-k], nums[k:]):
            a.pop(bisect.bisect_left(a, i))
            bisect.insort(a, j)
            res.append(median(a))
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().medianSlidingWindow1(nums, k))
