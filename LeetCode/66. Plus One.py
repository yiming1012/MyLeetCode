'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了42.83%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了23.56%的用户
        :param digits:
        :return:
        '''
        flag = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                flag, mod = divmod(digits[i] + 1 + flag, 10)
                digits[i] = mod
            else:
                if flag == 0:
                    return digits
                else:
                    flag, mod = divmod(digits[i] + flag, 10)
                    digits[i] = mod
        if flag == 1:
            digits.insert(0, 1)
        return digits

    def plusOne2(self, digits: List[int]) -> List[int]:
        '''
        执行用时 :28 ms, 在所有 Python3 提交中击败了96.08%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了23.56%的用户
        :param digits:
        :return:
        '''
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
        return digits


'''
加一只要为九就会有进位
'''
s = Solution()
arr = [1, 2, 9]
print(s.plusOne2(arr))
