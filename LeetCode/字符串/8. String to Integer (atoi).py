'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

'''
import re


class Solution:
    def myAtoi(self, str: str) -> int:
        # 去掉字符串昨天的空格
        str = str.lstrip()
        flag = 1
        res = 0
        if len(str) > 0:
            if str[0] == '-':
                flag = -1
                str = str[1:]
            elif str[0] == '+':
                flag = 1
                str = str[1:]
            if len(str) > 0 and (ord(str[0]) >= 48 and ord(str[0]) <= 57):
                for i in str:
                    if ord(i) >= 48 and ord(i) <= 57:
                        if (flag == 1 and (res > 2 ** 31 // 10 or (res == 2 ** 31 // 10 and int(i) > 7))):
                            return 2 ** 31 - 1
                        elif (flag == -1 and (res > 2 ** 31 // 10 or (res == 2 ** 31 // 10 and int(i) > 8))):
                            return -2 ** 31
                        else:
                            res = res * 10 + int(i)
                    else:
                        break

                return res * flag

        return 0

    def myAtoi2(self, str: str) -> int:
        return int(*re.findall('^[\+\-]?\d', str.lstrip()))


    def myAtoi3(self, str: str) -> int:
        import re
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        matches = re.match('[ ]*([+-]?\d+)', str)  # 最终要的就是这一句了吧，正则重在搞定匹配的pattern
        if matches:
            res = int(matches.group(1))
            if res > INT_MAX:
                return INT_MAX
            elif res < INT_MIN:
                return INT_MIN
            else:
                return res
        else:
            return 0


INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1



    def myAtoi(self, str: str) -> int:
        '''
        有限机
        :param str:
        :return:
        '''
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans






s = Solution()
string1 = " 12"
string2 = " -12"
string3 = " -w12"
string4 = "-987654321321"
string5 = "  -213412341"
result = s.myAtoi3(string5)
print(result)
