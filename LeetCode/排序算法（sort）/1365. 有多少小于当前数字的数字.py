"""
给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。

以数组形式返回答案。

 

示例 1：

输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释：
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。
对于 nums[3]=2 存在一个比它小的数字：（1）。
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
示例 2：

输入：nums = [6,5,4,8]
输出：[2,1,0,3]
示例 3：

输入：nums = [7,7,7,7]
输出：[0,0,0,0]
 

提示：

2 <= nums.length <= 500
0 <= nums[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def smallerNumbersThanCurrent1(self, nums: List[int]) -> List[int]:
        """
        思路：排序+前缀和+哈希
        时间复杂度：O(NlogN)
        """
        arr = collections.Counter(nums)
        aa = sorted(arr.items(), key=lambda item: item[0])
        pre = 0
        dic = collections.defaultdict(lambda: 0)
        for i in range(len(aa)):
            k, v = aa[i]
            dic[k] = pre
            pre += v
        res = []
        for num in nums:
            res.append(dic[num])
        return res

    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        """
        思路：桶排序
        1、由于样本数据不大，且是整数，可以采用桶排序
        2、对应值的下标为小于其值的个数
        """
        arr = [0] * 101
        for num in nums:
            arr[num] += 1
        pre = 0
        for i, a in enumerate(arr):
            arr[i] = pre
            pre += a
        return [arr[i] for i in nums]


if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    print(Solution().smallerNumbersThanCurrent1(nums))
    print(Solution().smallerNumbersThanCurrent2(nums))
