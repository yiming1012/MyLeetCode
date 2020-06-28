'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-perfect-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        执行用时 :28 ms, 在所有 Python3 提交中击败了93.56%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了6.35%的用户
        :param num:
        :return:
        '''
        return int(num ** 0.5) ** 2 == num

    def isPerfectSquare2(self, num: int) -> bool:
        '''
        执行用时 :60 ms, 在所有 Python3 提交中击败了14.34%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了6.35%的用户
        思路：二分法
        :param num:
        :return:
        '''
        # return int(num**0.5)**2==num
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 < num:
                left = mid + 1
            elif mid ** 2 > num:
                right = mid - 1
            else:
                return True
        return False

    def isPerfectSquare3(self, num: int) -> bool:
        '''
        执行用时 :48 ms, 在所有 Python3 提交中击败了27.62%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了6.35%的用户
        思路：牛顿迭代法
        :param num:
        :return:
        '''
        x = num
        while x ** 2 > num:
            x = (x + num // x) // 2

        return x ** 2 == num