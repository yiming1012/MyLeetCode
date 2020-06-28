'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''


class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(s)):
            num = dict[s[i]]
            if i < len(s) - 1 and (
                    (s[i] == 'I' and s[i + 1] in ['V', 'X']) or (s[i] == 'X' and s[i + 1] in ['L', 'C']) or (
                    s[i] == 'C' and s[i + 1] in ['D', 'M'])):
                num = -num
            sum += num
        return sum

    def romanToInt2(self, s: str) -> int:
        '''
        执行用时 :60 ms, 在所有 Python3 提交中击败了45.31%的用户
        内存消耗 :13.3 MB, 在所有 Python3 提交中击败了20.08%的用户
        :param s:
        :return:
        '''
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(s)):
            num = dict[s[i]]
            if s[i] in ['I', 'X', 'C'] and i < len(s) - 1 and dict[s[i]] < dict[s[i + 1]]:
                num = -num
            sum += num
        return sum


if __name__ == '__main__':
    '''
    本题的关键在于：输入的罗马字符合法，
    如果左边的字符小于右边的字符时，组合的值等于右边减左边，所以可将左边小值变为负数，从左至右相加
    答案中说使用switch-case比dict快很多
    '''
    s = "MCMXCIV"
    a = Solution()
    print(a.romanToInt2(s))
