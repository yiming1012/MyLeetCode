'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
通过次数44,731提交次数70,288

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        思路：快慢指针
        1、通过下标获取下一个元素，存在重复的值，相当于链表有环
        2、第一次循环找到相遇的点，这个点不一定是链表的入口
        3、起点和相遇的点离链表交点的距离相等
        """
        left, right = nums[0], nums[nums[0]]
        while left != right:
            left = nums[left]
            right = nums[nums[right]]
        start = 0
        while start != left:
            start = nums[start]
            left = nums[left]
        return start

    def findDuplicate2(self, nums: List[int]) -> int:
        '''
        如果可以改变nums的话
        :param nums:
        :return:
        '''
        pre = 0
        while nums[0] != pre:
            pre = nums[0]
            nums[0] = nums[pre]
            nums[pre] = pre
        return nums[0]

    def findDuplicate3(self, nums: List[int]) -> int:
        """
        思路：二分法
        1、数组的元素范围[1,n],所以可以利用二分查找，令mid=(1+len(arr))//2
        2、遍历数组，如果不大于mid的数目大于mid，说明重复的值肯定在[left,mid]之间，反之在[mid+1,right]
        """
        left, right = 1, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left

    def findDuplicate4(self, nums: List[int]) -> int:
        """
        思路：位运算
        1 [0 0 1]  1 [0 0 1]
        2 [0 1 0]  2 [0 1 0]
        3 [0 1 1]  2 [0 1 0]
        4 [1 0 0]  4 [1 0 0]
                   3 [0 1 1]
        a: 1 2 2   b: 1 3 2
        可以看到,b中间3大于a中间的2，说明该位置上的数出现的次数大于一，记录每个比特位的状态，即为重复的值

        """
        res = 0
        for i in range(0, (len(nums) - 1).bit_length()):
            carry = 1 << i
            count1, count2 = 0, 0
            for n in range(1, len(nums)):
                count1 += carry & n

            for num in nums:
                count2 += carry & num

            if count2 > count1:
                res += 1 << i
        return res


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 5, 4]
    print(Solution().findDuplicate(nums))
    print(Solution().findDuplicate2(nums))
    print(Solution().findDuplicate3(nums))
    print(Solution().findDuplicate4(nums))
