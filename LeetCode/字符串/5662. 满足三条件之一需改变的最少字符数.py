"""
5662. 满足三条件之一需改变的最少字符数
给你两个字符串 a 和 b ，二者均由小写字母组成。一步操作中，你可以将 a 或 b 中的 任一字符 改变为 任一小写字母 。

操作的最终目标是满足下列三个条件 之一 ：

a 中的 每个字母 在字母表中 严格小于 b 中的 每个字母 。
b 中的 每个字母 在字母表中 严格小于 a 中的 每个字母 。
a 和 b 都 由 同一个 字母组成。
返回达成目标所需的 最少 操作数。



示例 1：

输入：a = "aba", b = "caa"
输出：2
解释：满足每个条件的最佳方案分别是：
1) 将 b 变为 "ccc"，2 次操作，满足 a 中的每个字母都小于 b 中的每个字母；
2) 将 a 变为 "bbb" 并将 b 变为 "aaa"，3 次操作，满足 b 中的每个字母都小于 a 中的每个字母；
3) 将 a 变为 "aaa" 并将 b 变为 "aaa"，2 次操作，满足 a 和 b 由同一个字母组成。
最佳的方案只需要 2 次操作（满足条件 1 或者条件 3）。
示例 2：

输入：a = "dabadd", b = "cda"
输出：3
解释：满足条件 1 的最佳方案是将 b 变为 "eee" 。


提示：

1 <= a.length, b.length <= 105
a 和 b 只由小写字母组成
"""


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        """
        注意边界“z"的判断
        @param a:
        @param b:
        @return:
        """
        res = float('inf')
        for i in range(26):
            c = chr(97 + i)
            cnt = 0
            # a中所有值<=c b中所有值>c
            if c < 'z':
                for aa in a:
                    if aa > c:
                        cnt += 1
                for bb in b:
                    if bb <= c:
                        cnt += 1
                res = min(res, cnt)

            cnt = 0
            # a中所有值>c b中所有值<=c
            if c < 'z':
                for aa in a:
                    if aa <= c:
                        cnt += 1
                for bb in b:
                    if bb > c:
                        cnt += 1
                res = min(res, cnt)

            cnt = 0
            # a中所有值==c b中所有值==c
            for aa in a:
                if aa != c:
                    cnt += 1
            for bb in b:
                if bb != c:
                    cnt += 1
            res = min(res, cnt)

        return res


if __name__ == '__main__':
    a = "aba"
    b = "caa"
    print(Solution().minCharacters(a, b))
