"""
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

 

示例 1：

输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：

输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
示例 3：

输入：name = "leelee", typed = "lleeelee"
输出：true
示例 4：

输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。
 

提示：

name.length <= 1000
typed.length <= 1000
name 和 typed 的字符都是小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/long-pressed-name
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import itertools


class Solution:
    def isLongPressedName1(self, name: str, typed: str) -> bool:
        """
        思路：
        1. 通过itertools.groupby统计每个字符连续出现的次数
        2. 将字符串name和typed对应的字符k和连续出现的频次v存储到列表a,b中
        3. 如果a和b的长度不同，返回False
        4. 如果a和b的长度相同，则判断每一位的字符是否相同且b中的个数是否大于等于a中
        @param name:
        @param typed:
        @return:
        """
        a = [(k, len(list(v))) for k, v in itertools.groupby(name)]
        b = [(k, len(list(v))) for k, v in itertools.groupby(typed)]

        if len(a) != len(b):
            return False
        n = len(a)

        for i in range(n):
            ka, va = a[i]
            kb, vb = b[i]
            if ka != kb or va > vb:
                return False
        return True

    def isLongPressedName2(self, name: str, typed: str) -> bool:
        """
        思路：双指针
        1. 判断name和typed字符串的长度
        @param name:
        @param typed:
        @return:
        """
        m, n = len(name), len(typed)
        if m > n:
            return False
        left, right = 0, 0
        while right < n:
            if left < m and name[left] == typed[right]:
                left += 1
                right += 1
            elif right > 0 and typed[right] == typed[right - 1]:
                right += 1
            else:
                return False

        return left == m


if __name__ == '__main__':
    name = "alex"
    typed = "aaleex"
    print(Solution().isLongPressedName1(name, typed))
    print(Solution().isLongPressedName2(name, typed))
