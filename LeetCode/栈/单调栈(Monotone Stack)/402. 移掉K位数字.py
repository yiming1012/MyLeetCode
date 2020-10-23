"""
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。
示例 1 :

输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
示例 2 :

输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 :

输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-k-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def removeKdigits1(self, num: str, k: int) -> str:
        """
        思路：单调栈
        1. 如果k>0且前面数字比当前的大，pop出前面数字
        2. 如果遍历完后，k仍大于0，说明stack中的数字已经有序，删掉末尾k为数
        3. 如果最后的数不为"0"且包含前导0，将前面的0删除
        @param num:
        @param k:
        @return:
        """
        numStack = []

        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        finalStack = numStack[:-k] if k else numStack

        # trip the leading zeros
        return "".join(finalStack).lstrip('0') or "0"

    def removeKdigits2(self, num: str, k: int) -> str:
        stack = []
        for i, c in enumerate(num):
            while k and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)

        # 判断是否k个都删除完毕
        while k:
            stack.pop()
            k -= 1
        # 判断stack是否为空
        if not stack:
            return "0"

        # 判断前导0且至少保留最后一位
        index = 0
        while index < len(stack) - 1:
            if stack[index] != "0":
                break
            index += 1
        return "".join(stack[index:])


if __name__ == '__main__':
    num = "1432219"
    k = 3
    print(Solution().removeKdigits1(num, k))
    print(Solution().removeKdigits2(num, k))
