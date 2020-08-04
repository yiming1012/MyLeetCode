"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        思路：模拟
        1. 每轮加上进位
        2. 如果某一个字符串遍历完用0代替
        """
        carry = 0
        dic = {str(i): i for i in range(10)}
        n1, n2 = len(num1) - 1, len(num2) - 1
        res = ""
        while n1 >= 0 or n2 >= 0 or carry:
            s1 = dic[num1[n1]] if n1 >= 0 else 0
            s2 = dic[num2[n2]] if n2 >= 0 else 0
            s = s1 + s2 + carry
            carry, num = divmod(s, 10)
            res = str(num) + res
            n1 -= 1
            n2 -= 1
        return res


if __name__ == '__main__':
    num1, num2 = "123", "987"
    print(Solution().addStrings(num1, num2))
