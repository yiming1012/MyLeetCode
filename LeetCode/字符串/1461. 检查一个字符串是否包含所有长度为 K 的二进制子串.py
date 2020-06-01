"""
给你一个二进制字符串 s 和一个整数 k 。

如果所有长度为 k 的二进制字符串都是 s 的子串，请返回 True ，否则请返回 False 。

 

示例 1：

输入：s = "00110110", k = 2
输出：true
解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
示例 2：

输入：s = "00110", k = 2
输出：true
示例 3：

输入：s = "0110", k = 1
输出：true
解释：长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。
示例 4：

输入：s = "0110", k = 2
输出：false
解释：长度为 2 的二进制串 "00" 没有出现在 s 中。
示例 5：

输入：s = "0000000001011100", k = 4
输出：false
 

提示：

1 <= s.length <= 5 * 10^5
s 中只含 0 和 1 。
1 <= k <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        def dfs(ss, index):
            if len(ss) == k:
                res.append(ss)
                return

            for i in range(index, k):
                for j in "01":
                    dfs(ss + j, i + 1)

        res = []
        dfs("", 0)
        for c in res:
            if not c in s:
                return False
        return True

    def hasAllCodes2(self, s: str, k: int) -> bool:
        has = set()
        for i in range(len(s) - k + 1):
            has.add(s[i:i + k])

        return len(has) == 1 << k
        # return len(set(s[i:i + k] for i in range(len(s) - k + 1))) == 2 ** k


if __name__ == '__main__':
    s = "00110110"
    k = 2
    print(Solution().hasAllCodes(s, k))
    print(Solution().hasAllCodes2(s, k))

