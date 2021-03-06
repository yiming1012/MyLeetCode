'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-and-say
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了71.56%的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.21%的用户
        :param n:
        :return:
        '''
        s = "1"
        while n > 1:
            n -= 1
            s = ''.join(str(len(list(v)))+k for k, v in itertools.groupby(s))

        print(s)


if __name__ == '__main__':
    n = 2
    s = Solution()
    print(s.countAndSay(n))
