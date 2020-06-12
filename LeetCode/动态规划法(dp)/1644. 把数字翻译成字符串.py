"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 231

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def translateNum(self, num: int) -> int:
        """
        思路：动态规划法
        1. 类似青蛙跳台阶
        """
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            a, b = (a + b if "10" <= s[i - 2:i] <= "25" else a), a
        return a

    def translateNum2(self, num: int) -> int:
        """
        思路：动态规划法
        1. 如果当前的数和前一个数组成的整数在[10,25]区间内，可以看成是青蛙跳台阶，i-2跳到i的方案数：dp[i]=dp[i-1]+dp[i-2]
        """
        num = str(num)
        n = len(num)
        dp = [1] * (n + 1)
        for i in range(1, n):
            dp[i + 1] = dp[i]
            if 10 <= int(num[i - 1:i + 1]) <= 25:
                dp[i + 1] += dp[i - 1]

        return dp[-1]

    def translateNum3(self, num: int) -> int:
        """
        思路：
        """
        num = str(num)
        n = len(num)
        if n==0:
            return 1
        res = []
        dic = [chr(97 + i) for i in range(26)]
        print(dic)

        def dfs(S, index):
            if index == n - 1:
                print(S)
                Copy=S
                res.append(Copy)
                return
            for i in range(index + 1, n):
                dfs(S + dic[int(num[i])], i)
                if i < n - 1 and 10 <= int(num[i] + num[i + 1]) <= 25:
                    dfs(S + dic[int(num[i] + num[i + 1])], i)

        dfs(dic[num[0]], 0)
        return res

    def translateNum4(self, num: int) -> int:
        num = str(num)
        res = []

        def transform(i):
            return chr(int(i) + ord('a'))

        def dfs(i, word):
            if i == len(num):
                res.append(word)
                return
            dfs(i + 1, word + transform(num[i]))
            if i < len(num) - 1 and 9 < int(num[i:i + 2]) < 26:
                dfs(i + 2, word + transform(num[i:i + 2]))
            return

        dfs(1, transform(num[0]))
        if 9 < int(num[:2]) < 26:
            dfs(2, transform(num[:2]))
        return res


if __name__ == '__main__':
    num = 12258
    print(Solution().translateNum(num))
    print(Solution().translateNum2(num))
    print(Solution().translateNum3(num))
