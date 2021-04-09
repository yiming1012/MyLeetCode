"""
166. 分数到小数
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

如果小数部分为循环小数，则将循环的部分括在括号内。

如果存在多个答案，只需返回 任意一个 。

对于所有给定的输入，保证 答案字符串的长度小于 104 。

 

示例 1：

输入：numerator = 1, denominator = 2
输出："0.5"
示例 2：

输入：numerator = 2, denominator = 1
输出："2"
示例 3：

输入：numerator = 2, denominator = 3
输出："0.(6)"
示例 4：

输入：numerator = 4, denominator = 333
输出："0.(012)"
示例 5：

输入：numerator = 1, denominator = 5
输出："0.2"
 

提示：

-231 <= numerator, denominator <= 231 - 1
denominator != 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def fractionToDecimal(self, num: int, d: int) -> str:
        # 是否为0
        # 正负号
        # 整数部分
        # 小数部分
        if num == 0: return "0"
        res = []
        if (num > 0) ^ (d > 0) == 1: res.append("-")
        num, d = abs(num), abs(d)
        num, m = divmod(num, d)
        res.append(str(num))
        if m == 0:
            return "".join(res)
        # 存在小数
        res.append(".")
        dic = {m: len(res)}
        while m:
            m *= 10
            k, m = divmod(m, d)
            res.append(str(k))
            if m in dic:
                index = dic[m]
                # print(res)
                return "".join(res[:index]) + "(" + "".join(res[index:]) + ")"

            if m == 0:
                return "".join(res)
            dic[m] = len(res)

        """
        if numerator == 0: return "0"
        res = []
        # 首先判断结果正负, 异或作用就是 两个数不同 为 True 即 1 ^ 0 = 1 或者 0 ^ 1 = 1
        if (numerator > 0) ^ (denominator > 0):
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        # 判读到底有没有小数
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        # 无小数
        if b == 0:
            return "".join(res)
        res.append(".")
        # 处理余数
        # 把所有出现过的余数记录下来
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            # 余数前面出现过,说明开始循环了,加括号
            if b in loc:
                res.insert(loc[b], "(")
                res.append(")")
                break
            # 在把该位置的记录下来
            loc[b] = len(res)
        return "".join(res)
        """