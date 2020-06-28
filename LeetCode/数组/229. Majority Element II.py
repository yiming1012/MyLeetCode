'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        执行用时 :6700 ms, 在所有 Python3 提交中击败了5.34%的用户
        内存消耗 :14.2 MB, 在所有 Python3 提交中击败了6.74%的用户
        :param nums:
        :return:
        '''
        threshold = len(nums) // 3
        num = list(set(nums))
        for i in range(threshold):
            for j in num:
                # print(j)
                if j in nums:
                    nums.remove(j)

        return list(set(nums))

    def majorityElement2(self, nums: List[int]) -> List[int]:
        '''
        执行用时 :60 ms, 在所有 Python3 提交中击败了82.04%的用户
        内存消耗 :14.1 MB, 在所有 Python3 提交中击败了6.74%的用户
        :param nums:
        :return:
        '''
        if nums == []:
            return []
        threshold = len(nums) // 3
        nums.sort()
        arr = []
        start = nums[0]
        count = 0
        for i in range(len(nums)):
            if start == nums[i]:
                count += 1
            else:
                if count > threshold:
                    arr.append(nums[i - 1])
                start = nums[i]
                count = 1

            if i == len(nums) - 1 and count > threshold:
                arr.append(nums[i])

        return arr

    def majorityElement3(self, nums: List[int]) -> List[int]:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了94.66%的用户
        内存消耗 :14.3 MB, 在所有 Python3 提交中击败了6.74%的用户
        :param nums:
        :return:
        '''
        return [i for i in set(nums) if nums.count(i) > len(nums) / 3]

    def majorityElement4(self, nums: List[int]) -> List[int]:
        '''
        执行用时 :80 ms, 在所有 Python3 提交中击败了75.08%的用户
        内存消耗 :14.3 MB, 在所有 Python3 提交中击败了6.74%的用户
        摩尔投票法变种：超过三分之一，所以至多有2个。
        1、选择两个数num1和num2分别标记为最大，遇到相同的+1，两者都不同-1
        2、当count等于0时，num=i,count=1
        3、当遍历完成之后，判断个数是否超过三分之一
        :param nums:
        :return:
        '''
        if len(nums) == 0:
            return nums
        num1 = num2 = nums[0]
        count1 = count2 = 0
        for i in nums:
            if i == num1:
                count1 += 1
                continue
            if i == num2:
                count2 += 1
                continue
            if count1 == 0:
                num1 = i
                count1 = 1
                continue
            if count2 == 0:
                num2 = i
                count2 = 1
                continue
            count1 -= 1
            count2 -= 1

        count1 = count2 = 0
        for i in nums:
            if i == num1:
                count1 += 1
            elif i == num2:
                count2 += 1

        arr = []
        if count1 > len(nums) // 3:
            arr.append(num1)
        if count2 > len(nums) // 3:
            arr.append(num2)
        return arr


if __name__ == '__main__':
    nums = [2, 3, 4, 3]
    s = Solution()
    print(s.majorityElement3(nums))
