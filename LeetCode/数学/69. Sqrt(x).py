'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        执行用时 :8272 ms, 在所有 Python3 提交中击败了5.01%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.09%的用户
        :param x:
        :return:
        '''
        i = 0
        while i ** 2 <= x:
            i += 1
        return i if i ** 2 == x else i - 1
        # return int(x ** 0.5)

    def mySqrt2(self, x: int) -> int:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了66.27%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.20%的用户
        思路：二分法
        :param x:
        :return:
        '''
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 < x:
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1
            else:
                return mid
        return right

    def mySqrt3(self, x: int) -> int:
        '''
        执行用时 :48 ms, 在所有 Python3 提交中击败了54.34%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.20%的用户
        思路：牛顿迭代法
        :param x:
        :return:
        '''
        y = x
        while y ** 2 > x:
            y = (y + x // y) // 2

        return y


if __name__ == '__main__':
    x = 10
    print(Solution().mySqrt(x))
