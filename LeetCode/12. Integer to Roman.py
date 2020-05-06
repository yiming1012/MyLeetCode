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
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''


class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        执行用时 :52 ms, 在所有 Python3 提交中击败了76.01%的用户
        内存消耗 :13.3 MB, 在所有 Python3 提交中击败了21.05%的用户
        :param num:
        :return:
        '''
        dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        carry = 1
        s = ""
        while num > 0:
            num, mod = divmod(num, 10)
            if mod == 0:
                carry *= 10
                continue
            elif 0 < mod < 4:
                char = dict[carry]
                s = char * mod + s

            elif mod == 4:
                char = dict[carry]
                v = dict[5 * carry]
                s = char + v + s

            elif 4 < mod < 9:
                char = dict[carry]
                v = dict[5 * carry]
                s = v + (mod - 5) * char + s

            elif mod == 9:
                char = dict[carry]
                v = dict[10 * carry]
                s = char + v + s

            carry *= 10
        return s

    def intToRoman2(self, num: int) -> str:
        '''
        执行用时 :64 ms, 在所有 Python3 提交中击败了38.13%的用户
        内存消耗 :13.5 MB, 在所有 Python3 提交中击败了21.05%的用户
        :param self:
        :param num:
        :return:
        '''
        # 使用哈希表，按照从大到小顺序排列
        dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                5: 'V', 4: 'IV', 1: 'I'}
        s = ""
        for i in dict:
            if num >= i:
                div, num = divmod(num, i)
                s += div * dict[i]
            if num == 0:
                return s
        return s
'''
1、第一种方法针对特殊值进行分段：0,1-3,4,5-8,9.针对每一种情况进行分析
2、第二种方法是面额大小，从大到小遍历，每次计算商和余，该数为 商*面额对应的罗马字符，余数为0退出
'''

if __name__ == '__main__':
    num = 1994
    s = Solution()
    print(s.intToRoman2(num))