"""
给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。

「超赞子字符串」需满足满足下述两个条件：

该字符串是 s 的一个非空子字符串
进行任意次数的字符交换后，该字符串可以变成一个回文字符串
 

示例 1：

输入：s = "3242415"
输出：5
解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"
示例 2：

输入：s = "12345678"
输出：1
示例 3：

输入：s = "213123"
输出：6
解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"
示例 4：

输入：s = "00"
输出：2
 

提示：

1 <= s.length <= 10^5
s 仅由数字组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-longest-awesome-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestAwesome(self, s: str) -> int:
        """
        思路：位运算
        1. 能够组成回文的字符串，每个字母的个数必须全为偶数个或者有且仅有一个字符出现奇数次
        2. 仅包含数字就可以用位运算，长度为10的字符串
        @param s:
        @return:
        """
        dic = {0: -1}
        status = 0
        res = 0
        for i, c in enumerate(s):
            status ^= 1 << int(c)
            if status in dic:
                res = max(res, i - dic[status])
            else:
                dic[status] = i

            for j in range(10):
                pre = status ^ (1 << int(j))
                if pre in dic:
                    res = max(res, i - dic[pre])

        return res


if __name__ == '__main__':
    s = "1233214"
    print(Solution().longestAwesome(s))
