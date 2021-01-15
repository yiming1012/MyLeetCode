"""
1156. 单字符重复子串的最大长度
如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。

给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。



示例 1：

输入：text = "ababa"
输出：3
示例 2：

输入：text = "aaabaaa"
输出：6
示例 3：

输入：text = "aaabbaaa"
输出：4
示例 4：

输入：text = "aaaaa"
输出：5
示例 5：

输入：text = "abcdef"
输出：1


提示：

1 <= text.length <= 20000
text 仅由小写英文字母组成。
"""
import itertools
from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        arr = [(k, len(list(v))) for k, v in itertools.groupby(text)]
        cnt = Counter(text)
        m = len(arr)
        res = float('-inf')

        for i in range(m):
            k, v = arr[i]
            if v == 1:
                a, b, c = 0, 0, 0
                if i > 0:
                    k, a = arr[i - 1]
                    if cnt[k] > a:
                        a += 1

                if i < m - 1:
                    k, b = arr[i + 1]
                    if cnt[k] > b:
                        b += 1

                if 0 < i < m - 1 and arr[i - 1][0] == arr[i + 1][0]:
                    k1, v1 = arr[i - 1]
                    k2, v2 = arr[i + 1]
                    c = v1 + v2
                    if cnt[k1] > c:
                        c += 1
                res = max(res, a, b, c)
            else:
                k, v = arr[i]
                if cnt[k] > v:
                    v += 1
                res = max(res, v)
        return res


if __name__ == '__main__':
    text = "ababa"
    print(Solution().maxRepOpt1(text))
