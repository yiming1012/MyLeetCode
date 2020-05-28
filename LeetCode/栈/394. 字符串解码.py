"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        res = ""
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((res, num))
                res, num = "", 0
            elif c == "]":
                top = stack.pop()
                res = top[0] + res * top[1]
            else:
                res += c
        return res

    def decodeString2(self, s: str) -> str:
        """
        思路：模拟栈
        1. 栈每次记录前面排好的字符串和【】前面的数字
        """
        arr = []
        res = ""
        n = 0
        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
            elif c == '[':
                arr.append((n, res))
                res, n = "", 0
            elif c == ']':
                top = arr.pop()
                res = top[1] + top[0] * res

            else:
                res += c
        return res


if __name__ == '__main__':
    s = "ab3[a2[c]]"
    print(Solution().decodeString(s))
    print(Solution().decodeString2(s))
