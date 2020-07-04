"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        """
        思路：动态规划法+栈
        1. 栈用来存每一个没有匹配到的"("，如果匹配到了就弹出栈
        2. 动态规划数组用来存储当前字符结尾的字符串，能够成的最大有小括号的长度
        3.
        """
        dp = [0] * (len(s) + 1)
        stack = []
        res = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif stack:
                pre = stack.pop()
                dp[i + 1] = dp[pre] + 2 + dp[i]
                res = max(res, dp[i + 1])
        return res

    def longestValidParentheses2(self, s: str) -> int:
        """
        思路：栈
        1. 栈用来存每一个没有匹配到的"("，如果匹配到了就弹出栈
        2. 计算当前i与栈顶元素的距离，计算距离最大值
        """
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res


if __name__ == '__main__':
    s = "()(((((()))))((()"
    print(Solution().longestValidParentheses1(s))
    print(Solution().longestValidParentheses2(s))
