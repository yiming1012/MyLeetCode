'''
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        '''
        执行用时 :188 ms, 在所有 Python3 提交中击败了28.22%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了10.00%的用户
        思路：
        1、通过两层for循环查找每次的前两个数
        2、第三个数在后面的字符串中寻找，如果前两个数的长度的最大值大于剩余长度，返回
        3、如果数字以0开头且长度大于1，返回
        4、如果num1>2**31-1-num2，返回
        5、如果获得第三个数之后，剩余字符串为""，正确
        :param S:
        :return:
        '''
        def isValid(num1, num2, remain, arr):
            if num1[0] == '0' and len(num1) > 1: return False, arr
            if num2[0] == '0' and len(num2) > 1: return False, arr
            if int(num2) > 2 ** 31 - 1 - int(num1):
                return False, arr
            num3 = str(int(num1) + int(num2))

            if remain.startswith(num3):
                arr.append(num3)
                num1, num2 = num2, num3
                remain = remain[len(num3):]
                if remain == "":
                    return True, arr
                return isValid(num1, num2, remain, arr)
            return False, arr

        n = len(S)
        for i in range(1, n + 1 >> 1):
            arr = []
            num1 = S[:i]
            arr.append(num1)
            for j in range(i + 1, n):
                num2 = S[i:j]
                arr.append(num2)
                remain = S[j:]
                a, b = isValid(num1, num2, remain, arr)
                if a:
                    return arr
                else:
                    arr.pop()
        return []

    def splitIntoFibonacci2(self, S: str) -> List[int]:
        def backtrack(index, fib, next_num):
            if index == len(S) and len(fib) > 2:
                return fib
            for i in range(index, len(S)):
                num_str = S[index:i + 1]
                if num_str[0] == '0' and len(num_str) > 1:
                    continue
                num = int(num_str)
                if int(num) > 2 ** 31 - 1:
                    break
                if len(fib) < 2:
                    fib.append(num)
                elif num == next_num:
                    fib.append(num)
                elif num > next_num:
                    break
                else:
                    continue
                res = backtrack(i + 1, fib, next_num if len(fib) < 2 else fib[-2] + fib[-1])
                if res:
                    return res
                fib.pop()

        return backtrack(0, [], 0)


if __name__ == '__main__':
    # num = "123456579"
    num = "1203"
    s = Solution()
    print(s.splitIntoFibonacci2(num))
