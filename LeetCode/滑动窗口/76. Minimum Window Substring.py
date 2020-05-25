"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        此方法超时
        """
        ns = len(s)
        nt = len(t)
        tt = collections.Counter(t)

        for i in range(nt, ns + 1):
            for j in range(0, ns + 1 - i):
                window = s[j:j + i]
                ss = collections.Counter(window)
                for k, v in tt.items():
                    if k not in ss or ss[k] < v:
                        break
                else:
                    return window
        return ""

    def minWindow2(self, s: str, t: str) -> str:
        """
        执行用时 :720 ms, 在所有 Python3 提交中击败了11.95%的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了7.69%的用户
        思路：滑动窗口
        1、维护两个指针left和right
        2、right向右遍历到整个字符串包含t,再移动left使得包含的长度最小
        3、利用dict保存遍历过的每个字符的个数
        """

        tt = collections.Counter(t)
        left, right = 0, 0
        minLen = float('inf')
        start, end = -1, -1
        dic = collections.defaultdict(lambda: 0)

        while right < len(s):
            dic[s[right]] += 1
            while right - left + 1 >= len(t) and all([dic[k] >= tt[k] for k in tt]):
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start, end = left, right
                dic[s[left]] -= 1
                left += 1
            right += 1
        return s[start:end + 1] if start != -1 else ""



