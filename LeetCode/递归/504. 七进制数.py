"""
504. 七进制数
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/base-7
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def convertToBase7_1(self, num: int) -> str:

        def dfs(num):
            if num < 0: return '-' + dfs(-num)
            if num < 7: return str(num)
            return dfs(num // 7) + str(num % 7)

        return dfs(num)

    def convertToBase7_2(self, num: int) -> str:
        if num == 0:
            return "0"

        flag = ""
        stack = []
        if num < 0:
            flag = '-'
            num = -num

        while num:
            stack.append(str(num % 7))
            num //= 7

        return flag + "".join(stack[::-1])


if __name__ == '__main__':
    num = 100
    print(Solution().convertToBase7_1(num))
    print(Solution().convertToBase7_2(num))
