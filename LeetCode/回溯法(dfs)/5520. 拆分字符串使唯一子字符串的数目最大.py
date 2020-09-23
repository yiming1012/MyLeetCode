"""
给你一个字符串 s ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。

字符串 s 拆分后可以得到若干 非空子字符串 ，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是 唯一的 。

注意：子字符串 是字符串中的一个连续字符序列。



示例 1：

输入：s = "ababccc"
输出：5
解释：一种最大拆分方法为 ['a', 'b', 'ab', 'c', 'cc'] 。像 ['a', 'b', 'a', 'b', 'c', 'cc'] 这样拆分不满足题目要求，因为其中的 'a' 和 'b' 都出现了不止一次。
示例 2：

输入：s = "aba"
输出：2
解释：一种最大拆分方法为 ['a', 'ba'] 。
示例 3：

输入：s = "aa"
输出：1
解释：无法进一步拆分字符串。


提示：

1 <= s.length <= 16

s 仅包含小写英文字母
"""


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        """
        思路：回溯法
        1. 通过visited哈希表记录当前拆分的单词是否前面拆分的单词相同
        2. 每次拆分完后对剩余的字符串进行相同操作
        3. 如果剩余的字符串为空，则求出拆分的最大单词个数
        @param s:
        @return:
        """
        n = len(s)
        visited = set()
        res = 1

        def dfs(left):
            if len(left) == 0:
                nonlocal res
                res = max(res, len(visited))
                return

            for i in range(1, len(left) + 1):
                if left[:i] not in visited:
                    visited.add(left[:i])
                    dfs(left[i:])
                    visited.remove(left[:i])

        dfs(s)
        return res


if __name__ == '__main__':
    s = "ababccc"
    print(Solution().maxUniqueSplit(s))
