"""
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

 

Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
 

Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """
        执行用时 :824 ms, 在所有 Python3 提交中击败了85.96%的用户
        内存消耗 :17.4 MB, 在所有 Python3 提交中击败了50.00%的用户
        思路：
        1、判断B中所有元素都是A中的子集，可以先把B的特征提取出来，比如每个元素出现的次数，["oo","lo"]，B的特征dic={'o':2,'l':1}
        2、提取A中每个单词的特征，分别与B的特征对比，如果B中的元素在A中出现的次数均不大于B中的次数，则该单词满足条件
        """
        dicB = collections.defaultdict(lambda: 0)
        # 提取B的特征
        for b in B:
            for k, v in collections.Counter(b).items():
                if dicB[k] < v:
                    dicB[k] = v

        res = []
        for a in A:
            aa = collections.Counter(a)
            for k in dicB:
                if aa[k] < dicB[k]:
                    break
            else:
                res.append(a)
        return res


if __name__ == '__main__':
    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["ec", "oc", "ceo"]
    print(Solution().wordSubsets(A, B))
