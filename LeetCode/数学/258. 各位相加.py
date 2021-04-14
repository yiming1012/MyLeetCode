"""
258. 各位相加
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:

输入: 38
输出: 2
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
进阶:
你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def addDigits(self, num: int) -> int:
        """
        方法一：递归
        @param num:
        @return:
        """
        def dfs(num):
            if num<=9:
                return num
            return dfs(dfs(num//10)+num%10)
        res=dfs(num)
        return res

    def addDigits(self, num: int) -> int:
        """
        方法二：数学O(1)
        @param num:
        @return:
        """
        if not num:return 0
        return (num-1)%9+1
