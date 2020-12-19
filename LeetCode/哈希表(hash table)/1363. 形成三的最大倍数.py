"""
1363. 形成三的最大倍数
给你一个整数数组 digits，你可以通过按任意顺序连接其中某些数字来形成 3 的倍数，请你返回所能得到的最大的 3 的倍数。

由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。

如果无法得到答案，请返回一个空字符串。



示例 1：

输入：digits = [8,1,9]
输出："981"
示例 2：

输入：digits = [8,6,7,1,0]
输出："8760"
示例 3：

输入：digits = [1]
输出：""
示例 4：

输入：digits = [0,0,0,0,0,0]
输出："0"


提示：

1 <= digits.length <= 10^4
0 <= digits[i] <= 9
返回的结果不应包含不必要的前导零。
"""
import collections
from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        dic = collections.defaultdict(list)
        for i, d in enumerate(digits):
            dic[d % 3].append(i)

        digits = list(map(str, digits))
        s = sum(map(int, digits))
        if s % 3 == 0:
            res = "".join(digits).lstrip("0")
            return res if res else "0"

        elif s % 3 == 1:
            # 减去一个1或者两个2
            if len(dic[1]) >= 1:
                index = dic[1][-1]
                digits.pop(index)
                if digits:
                    res = "".join(digits).lstrip("0")
                    return res if res else "0"
                else:
                    return ""
            if len(dic[2]) >= 2:
                index1 = dic[2][-1]
                index2 = dic[2][-2]
                digits.pop(index1)
                digits.pop(index2)
                if digits:
                    res = "".join(digits).lstrip("0")
                    return res if res else "0"
                else:
                    return ""

        else:
            # 减去一个2或者两个1
            if len(dic[2]) >= 1:
                index = dic[2][-1]
                digits.pop(index)
                if digits:
                    res = "".join(digits).lstrip("0")
                    return res if res else "0"
                else:
                    return ""
            if len(dic[1]) >= 2:
                index1 = dic[1][-1]
                index2 = dic[1][-2]
                digits.pop(index1)
                digits.pop(index2)
                if digits:
                    res = "".join(digits).lstrip("0")
                    return res if res else "0"
                else:
                    return ""
        return ""


if __name__ == '__main__':
    digits = [8, 1, 9]
    print(Solution().largestMultipleOfThree(digits))
