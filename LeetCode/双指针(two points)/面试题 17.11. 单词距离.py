"""
面试题 17.11. 单词距离
有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

示例：

输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
输出：1
提示：

words.length <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-closest-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        """
        思路：双指针
        1. 现将两个单词出现的索引依次加入数组中
        2. 双指针排序两个数组中的索引，不停计算两个索引的差的绝对值
        @param words:
        @param word1:
        @param word2:
        @return:
        """
        dic = collections.defaultdict(list)
        for i, word in enumerate(words):
            dic[word].append(i)

        arr1 = dic[word1]
        arr2 = dic[word2]
        res = float('inf')
        i, j = 0, 0
        n, m = len(arr1), len(arr2)

        while i < n and j < m:
            res = min(res, abs(arr1[i] - arr2[j]))
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        return res


if __name__ == '__main__':
    words = ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"]
    word1 = "a"
    word2 = "student"
    print(Solution().findClosest(words, word1, word2))
