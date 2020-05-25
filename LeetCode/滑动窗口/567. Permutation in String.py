"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = collections.Counter(s1)
        dic2 = collections.defaultdict(lambda: 0)
        for i in range(len(s2)):
            dic2[s2[i]] += 1
            if i >= len(s1) - 1:
                if all(map(lambda x: dic[x] == dic2[x], dic.keys())):
                    return True

                dic2[s2[i - len(s1) + 1]] -= 1
        return False

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        """
        不用每次比较dict
        """
        if len(s1) > len(s2):
            return False
        s1_cnt = [0] * 26
        s2_cnt = [0] * 26
        for c in s1:
            s1_cnt[ord(c) - ord('a')] += 1
        j = 0
        for i in range(len(s2)):
            if i < len(s1) - 1:
                s2_cnt[ord(s2[i]) - ord('a')] += 1
                continue
            s2_cnt[ord(s2[i]) - ord('a')] += 1
            if s2_cnt == s1_cnt:
                return True
            s2_cnt[ord(s2[j]) - ord('a')] -= 1
            j += 1
        return False
