"""
224. 基本计算器
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。

 

示例 1：

输入：s = "1 + 1"
输出：2
示例 2：

输入：s = " 2-1 + 2 "
输出：3
示例 3：

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
 

提示：

1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
如果当前是数字，那么更新计算当前数字；
如果当前是操作符+或者-，那么需要更新计算当前计算的结果 res，并把当前数字 num 设为 0，sign 设为正负，重新开始；
如果当前是 ( ，那么说明遇到了右边的表达式，而后面的小括号里的内容需要优先计算，所以要把 res，sign 进栈，更新 res 和 sign 为新的开始；
如果当前是 ) ，那么说明右边的表达式结束，即当前括号里的内容已经计算完毕，所以要把之前的结果出栈，然后计算整个式子的结果；
最后，当所有数字结束的时候，需要把最后的一个 num 也更新到 res 中。
"""


class Solution:
    def calculate(self, s: str) -> int:
        """
        res:总和
        pre：当前式子的和
        sign：当前式子的符号
        stack：存储前面计算过的值和符号
        @param s:
        @return:
        """
        stack, res, pre, sign = [], 0, 0, 1
        for c in s:
            if c.isdigit():
                pre = pre * 10 + int(c)
            elif c in {'+', '-'}:
                res += pre * sign
                sign = 1 if c == '+' else -1
                pre = 0
            elif c == '(':
                res += pre * sign
                stack.extend([res, sign])
                res, sign = 0, 1
            elif c == ')':
                res += pre * sign
                res *= stack.pop()
                res += stack.pop()
                pre, sign = 0, 1
        res += pre * sign
        return res


if __name__ == '__main__':
    s = "(1+(4+5+2)-3)+(6+8)"  # 23
    print(Solution().calculate(s))
