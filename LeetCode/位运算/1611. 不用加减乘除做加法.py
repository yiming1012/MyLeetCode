'''
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

 

示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def add(self, a: int, b: int) -> int:
        '''
        执行用时 :40 ms, 在所有 Python3 提交中击败了59.84%的用户
        内存消耗 :13.4 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：
        ^:不进位的加法
        &：获取为两项都为1的位置，向左移位，再^相当于进位
        :param a:
        :param b:
        :return:
        '''
        maxInt = 2 ** 32 - 1
        print(maxInt)
        while b:
            a, b = (a ^ b) & maxInt, ((a & b) << 1) & maxInt
            # print(a,b)
        return a if a < 2 ** 31 else ~(a ^ maxInt)


if __name__ == '__main__':
    a, b = -2, 1
    print(Solution().add(a, b))
