'''
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Example 1:

Input: "aabcccccaaa"
Output: "a2b1c5a3"
Example 2:

Input: "abbccd"
Output: "abbccd"
Explanation:
The compressed string is "a1b2c2d1", which is longer than the original string.
 

Note:

0 <= S.length <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compress-string-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import itertools


class Solution:
    def compressString(self, S: str) -> str:
        '''
        执行用时 :96 ms, 在所有 Python3 提交中击败了22.00%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param S:
        :return:
        '''
        if len(S) <= 2:
            return S
        count = 0
        res = S[0]
        num = S[0]
        for i in range(len(S)):
            if S[i] == num:
                count += 1

            else:
                res += str(count)
                res += S[i]
                num = S[i]
                count = 1

            # if i == len(S) - 1:
            #     res += str(count)
        # 边界问题：可以不在for循环里面判断，提出来效率更高，从22%到66%
        res += str(count)

        return res if len(S) > len(res) else S

    def compressString(self, S: str) -> str:
        '''
        执行用时 :44 ms, 在所有 Python3 提交中击败了96.25%的用户
        内存消耗 :15.5 MB, 在所有 Python3 提交中击败了100.00%的用户
        :param S:
        :return:
        '''
        # s = ''.join(c + str(len(list(v))) for c, v in itertools.groupby(S))
        s = ''.join(c + str(len([*v])) for c, v in itertools.groupby(S))
        return len(s) < len(S) and s or S
