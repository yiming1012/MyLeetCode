"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous
subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/continuous-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        官方解题:前缀和+哈希
        1. 如果子数组和是k的倍数，那么他的余数也肯定在哈希表中
        :param nums:
        :param k:
        :return:
        """
        dic = {0: -1}
        pre = 0
        for i, num in enumerate(nums):
            pre += num
            if k != 0: pre %= k
            if pre in dic:
                if i - dic[pre] > 1:
                    return True
            else:
                dic[pre] = i
        return False


if __name__ == '__main__':
    nums = [1, 2, 3]
    k = 3
    s = Solution()
    print(s.checkSubarraySum(nums, k))
