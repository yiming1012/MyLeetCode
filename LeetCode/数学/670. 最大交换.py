"""
670. 最大交换
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。
注意:

给定数字的范围是 [0, 108]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-swap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        思路：数学
        1. 记录每个字符最后出现的索引
        2. 顺序遍历字符串，如果某个字符比当前字符大，且索引也大，就替换
        @param num:
        @return:
        """
        num = list(str(num))
        index = {}

        for i, c in enumerate(num):
            index[c] = i

        flag = False
        for i, c in enumerate(num):
            for j in range(9, -1, -1):
                k = index.get(str(j), -1)
                if str(j) > c and k > i:
                    num[i], num[k] = num[k], num[i]
                    flag = True
                    break
            if flag:
                break

        return int("".join(num))


if __name__ == '__main__':
    num = 9937
    print(Solution().maximumSwap(num))
