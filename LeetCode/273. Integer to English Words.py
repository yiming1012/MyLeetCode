'''

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''

class Solution:
    def numberToWords(self, num: int) -> str:
        dict = {1000000000: 'Billion',
                1000000: 'Million',
                1000: 'Thousand',
                100: 'Hundred',
                90: 'Ninety',
                80: 'Eighty',
                70: 'Seventy',
                60: 'Sixty',
                50: 'Fifty',
                40: 'Forty',
                30: 'Thirty',
                20: 'Twenty',
                19: 'Nineteen',
                18: 'Eighteen',
                17: 'Seventeen',
                16: 'Sixteen',
                15: 'Fifteen',
                14: 'Fourteen',
                13: 'Thirteen',
                12: 'Twelve',
                11: 'Eleven',
                10: 'Ten',
                9: 'Nine',
                8: 'Eight',
                7: 'Seven',
                6: 'Six',
                5: 'Five',
                4: 'Four',
                3: 'Three',
                2: 'Two',
                1: 'One'

                }
        # print(change(123))
        s = ""
        if num == 0:
            return 'Zero'
        if num >= 10 ** 9:
            n, num = divmod(num, 10 ** 9)
            s += self.change(dict, n) + ' ' + dict[10 ** 9]
        if num >= 10 ** 6:
            n, num = divmod(num, 10 ** 6)
            s += self.change(dict, n) + ' ' + dict[10 ** 6]
        if num >= 10 ** 3:
            n, num = divmod(num, 10 ** 3)
            s += self.change(dict, n) + ' ' + dict[10 ** 3]
        if num < 10 ** 3:
            s += self.change(dict, num)
        return s.lstrip()

    def change(self, dict, n):
        s = ""
        if n // 100 > 0:
            s += ' ' + dict[n // 100] + ' ' + dict[100]
            n %= 100
        if n in dict:
            s += ' ' + dict[n]
        else:
            n, m = divmod(n, 10)
            if m != 0:
                s += ' ' + dict[n * 10] + ' ' + dict[m]

        return s

    def numberToWords2(self, num: int) -> str:
        '''
        执行用时 :36 ms, 在所有 Python3 提交中击败了66.39%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了12.82%的用户
        :param num:
        :return:
        '''
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def helper(num):
            if num < 20:
                print("num<20",num,to19[num - 1:num])
                return to19[num - 1:num]
            if num < 100:
                print("num<100",num)
                return [tens[num // 10 - 2]] + helper(num % 10)
            if num < 1000:
                return [to19[num // 100 - 1]] + ["Hundred"] + helper(num % 100)
            for p, w in enumerate(["Thousand", "Million", "Billion"], 1):
                if num < 1000 ** (p + 1):
                    return helper(num // 1000 ** p) + [w] + helper(num % 1000 ** p)

        return " ".join(helper(num)) or "Zero"

'''
1、主要用分治法，123,456,789.每三位进行分析
2、第一种方法从高位到低位，通过字符串的形式把所有英文连起来
3、第二种方法分为1-19,20-90，从低位到高位，通过list将英文加起来最后join
4、巧妙之处在于：不把零放到list中，否则末尾会出现zero
'''



if __name__ == '__main__':
    num = 20
    s = Solution()
    print(s.numberToWords2(num))
