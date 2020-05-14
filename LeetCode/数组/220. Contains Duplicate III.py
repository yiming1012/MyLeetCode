'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the
absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        '''
        Time limit exceeded.
        :param nums:
        :param k:
        :param t:
        :return:
        '''
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if abs(i - j) <= k and abs(nums[i] - nums[j]) <= t:
                    return True

        return False

    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t: int) -> bool:
        '''
        Time limit exceeded.
        :param nums:
        :param k:
        :param t:
        :return:
        '''
        for i in range(1, len(nums)):
            for j in range(max(i - k, 0), i):
                if abs(nums[i] - nums[j]) <= t:
                    return True

        return False


    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        '''
        执行用时 :64 ms, 在所有 Python3 提交中击败了57.21%的用户
        内存消耗 :15.5 MB, 在所有 Python3 提交中击败了7.23%的用户
        思路：桶排序，通过空间换时间
        :param nums:
        :param k:
        :param t:
        :return:
        '''
        if t < 0 or k < 0:
            return False
        all_buckets = {}

        bucket_size = t + 1  # 桶的大小设成t+1更加方便
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size  # 放入哪个桶

            if bucket_num in all_buckets:  # 桶中已经有元素了
                return True

            all_buckets[bucket_num] = nums[i]  # 把nums[i]放入桶中

            if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t:  # 检查前一个桶
                return True

            if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t:  # 检查后一个桶
                return True

            # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过k
            if i >= k:
                all_buckets.pop(nums[i - k] // bucket_size)

        return False


if __name__ == '__main__':
    nums = [1, 0, 1, 1]
    k = 1
    t = 2
    s = Solution()
    print(s.containsNearbyAlmostDuplicate2(nums, k, t))
