"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 

限制：

1 <= n <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qiu-12n-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def sumNums(self, n: int) -> int:
        """
        思路：短路递归
        1. 利用and的性质：0 and 1
        """
        return n and n+self.sumNums(n-1)


if __name__ == '__main__':
    print(Solution().sumNums(10))