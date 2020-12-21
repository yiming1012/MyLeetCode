"""
1358. 包含所有三种字符的子字符串数目
给你一个字符串 s ，它只包含三种字符 a, b 和 c 。

请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。

 

示例 1：

输入：s = "abcabc"
输出：10
解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
示例 2：

输入：s = "aaacb"
输出：3
解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
示例 3：

输入：s = "abc"
输出：1
 

提示：

3 <= s.length <= 5 x 10^4
s 只包含字符 a，b 和 c 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-substrings-containing-all-three-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        思路：滑动窗口
        https://leetcode-cn.com/problems/number-of-substrings-containing-all-three-characters/solution/python3-shuang-zhi-zhen-shi-xian-hua-don-3kg0/
        @param s:
        @return:
        """
        dic = collections.defaultdict(lambda: 0)
        n = len(s)
        left, right = 0, -1
        res = 0

        while left < n and right < n:
            while dic["a"] > 0 and dic["b"] > 0 and dic["c"] > 0:
                res += n - right
                dic[s[left]] -= 1
                left += 1

            right += 1
            if right < n:
                dic[s[right]] += 1

        return res


if __name__ == '__main__':
    s = "abcabc"
    print(Solution().numberOfSubstrings(s))
