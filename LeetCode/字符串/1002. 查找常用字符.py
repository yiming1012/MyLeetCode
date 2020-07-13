"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

 

示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]
 

提示：

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-common-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def commonChars1(self, A: List[str]) -> List[str]:
        """
        思路：
        1. 通过哈希表存储第一个单词的字符频数，用这个dict去遍历后面每一个单词的Counter结果d
        2. 如果dict中的字符不在d中，删除；在，则取两者的更小值
        注意：dict删除元素时，不能直接在遍历中删除，需要变为list
        """
        res = []
        dic = collections.Counter(A[0])
        for i in range(1, len(A)):
            d = collections.Counter(A[i])
            for k in list(dic.keys()):
                if k not in d:
                    del dic[k]
                else:
                    dic[k] = min(dic[k], d[k])

        for k, v in dic.items():
            res += [k] * v
        res.sort()
        return res

    def commonChars2(self, A: List[str]) -> List[str]:
        k = collections.Counter(A[0])
        res = []
        for i in k:
            minNum = min(a.count(i) for a in A)
            res += [i] * minNum
        return res

    def commonChars3(self, A: List[str]) -> List[str]:
        """
        dict.elements()：dict中元素个数
        """
        from functools import reduce
        print(reduce(lambda x, y: x & y, map(collections.Counter, A)))
        return list(reduce(lambda x, y: x & y, map(collections.Counter, A)).elements())


if __name__ == '__main__':
    A = ["bella", "label", "roller"]
    print(Solution().commonChars1(A))
    print(Solution().commonChars2(A))
    print(Solution().commonChars3(A))
