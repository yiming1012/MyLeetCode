"""
给你一个整数 num 。你可以对它进行如下步骤恰好 两次 ：

选择一个数字 x (0 <= x <= 9).
选择另一个数字 y (0 <= y <= 9) 。数字 y 可以等于 x 。
将 num 中所有出现 x 的数位都用 y 替换。
得到的新的整数 不能 有前导 0 ，得到的新整数也 不能 是 0 。
令两次对 num 的操作得到的结果分别为 a 和 b 。

请你返回 a 和 b 的 最大差值 。

 

示例 1：

输入：num = 555
输出：888
解释：第一次选择 x = 5 且 y = 9 ，并把得到的新数字保存在 a 中。
第二次选择 x = 5 且 y = 1 ，并把得到的新数字保存在 b 中。
现在，我们有 a = 999 和 b = 111 ，最大差值为 888
示例 2：

输入：num = 9
输出：8
解释：第一次选择 x = 9 且 y = 9 ，并把得到的新数字保存在 a 中。
第二次选择 x = 9 且 y = 1 ，并把得到的新数字保存在 b 中。
现在，我们有 a = 9 和 b = 1 ，最大差值为 8
示例 3：

输入：num = 123456
输出：820000
示例 4：

输入：num = 10000
输出：80000
示例 5：

输入：num = 9288
输出：8700
 

提示：

1 <= num <= 10^8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-difference-you-can-get-from-changing-an-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        """
        思路：字符串操作，replace
        1. 求最大值时，只要当前位置不是9，将与该位置相同的字符替换为9
        2. 求最小值时，分两种情况
            1）如果首项不是1，将与该位置相同的字符替换为1
            2）如果首项为1，将后面第一个不为1的字符对应的所有字符替换为0
        """
        s1 = s2 = str(num)
        # print(s1,s2)
        # 最大值
        for c in s1:
            if c != "9":
                s1 = s1.replace(c, "9")
                break
        # print(s1)
        # 最小值
        for c in s2:
            if s2[0] != "1":
                s2 = s2.replace(c, "1")
                break
            elif c != "1" and c != "0":
                s2 = s2.replace(c, "0")
                break
        return int(s1) - int(s2)


if __name__ == '__main__':
    num = 555
    print(Solution().maxDiff(num))
