'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        执行用时 :176 ms, 在所有 Python3 提交中击败了44.68%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了22.81%的用户
        :param num1:
        :param num2:
        :return:
        '''
        sum = 0
        carry = 1
        flag = 1
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                a = int(num1[i])
                b = int(num2[j])
                sum += a * b * carry * flag
                carry *= 10
            flag *= 10
            carry = 1

        return str(sum)


num1 = "123"
num2 = "456"
s = Solution()
s.multiply(num1, num2)
