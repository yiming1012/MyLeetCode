"""
1371. 每个元音包含偶数次的最长子字符串
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

 

示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
 

提示：

1 <= s.length <= 5 x 10^5
s 只包含小写英文字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        执行用时 :884 ms, 在所有 Python3 提交中击败了40.81%的用户
        内存消耗 :19.8 MB, 在所有 Python3 提交中击败了100.00%的用户
        思路：状态压缩+前缀和+哈希表+位运算
        """
        dic = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        dp = {0: -1}
        flag = 0
        res = 0
        for i, c in enumerate(s):
            flag ^= dic.get(c, 0)
            print(flag)
            res = max(res, i - dp.setdefault(flag, i))
            print(i, dp)
        return res


    def findTheLongestSubstring2(self, s: str) -> int:
            ans, status, n = 0, 0, len(s)
            pos = [-1] * (1 << 5)
            pos[0] = 0
            print(pos)
            for i in range(n):
                if s[i] == 'a':
                    status ^= 1 << 0
                elif s[i] == 'e':
                    status ^= 1 << 1
                elif s[i] == 'i':
                    status ^= 1 << 2
                elif s[i] == 'o':
                    status ^= 1 << 3
                elif s[i] == 'u':
                    status ^= 1 << 4

                if pos[status] != -1:
                    ans = max(ans, i + 1 - pos[status])
                else:
                    pos[status] = i+1
            return ans

    """
    def findTheLongestSubstring3(self, s: str) -> int:
        # bit_mask由左至右对应 aeiou 5个元音字母的出现次数的奇偶性，
        # 1代表某个字母出现奇数次，0代表出现偶数次
        bit_mask = eval('0b00000')
        # 下面一行，初始化状态集，一开始元音字母都是0次(都为偶数)，这种情况发生在-1位置，即0位置的左侧
        # state_first_idx的含义为，某种状态(key)：第一次出现的位置(index)
        state_first_idx = {eval('0b00000'): -1}
        vowels = 'aeiou'
        ans = 0
        for i in range(len(s)):
            if (idx := vowels.find(s[i])) > -1:  # str的find方法，找不到返回-1，找到返回元素在字符串中的index，将找到的结果放在idx中
                bit_mask ^= eval('0b10000') >> idx  # 找到idx后，就要将对应位置进行翻转(用异或实现)
                # eval('0b10000') >> idx，就是将找到的元音所对应的那位设为1，
                # 它再和原始的 bit_mask 异或就实现了将元音对应位置翻转
            if bit_mask not in state_first_idx:  # 如果当前状态没有出现，则将其记录
                state_first_idx[bit_mask] = i
            ans = max(ans, i - state_first_idx[bit_mask])  # 更新结果
        return ans
    """


if __name__ == '__main__':
    a = "aba"
    print(Solution().findTheLongestSubstring(a))
    print(Solution().findTheLongestSubstring2(a))
