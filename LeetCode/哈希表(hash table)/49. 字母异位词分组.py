"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


class Solution:
    def groupAnagrams1(self, strs):
        """
        思路：哈希+tuple
        1. 对每个单词进行排序，使得key唯一
        2. 将list转换为可哈希的tuple，作为dict的key
        @param strs:
        @return:
        """
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

    def groupAnagrams2(self, strs):
        """
        思路：哈希+tuple
        1. 上面的方案中如果字符串长度很大，排序会比较耗时
        2. 通过长度为26的list记录每个字母出现的次数，最后转换成可哈希的tuple，作为dict的key
        @param strs:
        @return:
        """
        ans = collections.defaultdict(list)
        for s in strs:
            word = [0] * 26
            for c in s:
                word[ord(c) - 97] += 1
            ans[tuple(word)].append(s)
        return list(ans.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams1(strs))
    print(Solution().groupAnagrams2(strs))
