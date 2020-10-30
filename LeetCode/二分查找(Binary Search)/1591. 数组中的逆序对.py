'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
 

限制：

0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        思路：直接遍历会超时，需要用到二分
        :param nums:
        :return:
        '''
        # arr= []
        count = 0
        n = len(nums)
        if n <= 1:
            return 0
        arr = [nums[0]]
        # 找到第一个
        for i in range(1, n):
            low, high = 0, len(arr) - 1
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] <= nums[i]:
                    high = mid - 1
                else:
                    low = mid + 1
            print(low)
            count += low
            arr.append(nums[i])
            arr.sort(reverse=True)

        return count


if __name__ == '__main__':
    nums = [7, 5, 6, 4]
    s = Solution()
    # print(s.reversePairs(nums))

    nums = [4, 7, 5, 6, 4]
    for i in range(1, len(nums)):
        low, high = 0, i - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= nums[i]:
                high = mid - 1
            else:
                low = mid + 1
        print(low)

    import bisect


    def reversePairs(self, nums: List[int]) -> int:
        q = []
        res = 0
        for v in nums:
            i = bisect.bisect_left(q, -v)
            res += i
            q[i:i] = [-v]
        return res
