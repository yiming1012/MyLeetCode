"""
1202. 交换字符串中的元素
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。

 

示例 1:

输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"
示例 2：

输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"
示例 3：

输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1], s = "bca"
交换 s[1] 和 s[2], s = "bac"
交换 s[0] 和 s[1], s = "abc"
 

提示：

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s 中只含有小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-string-with-swaps
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = {i: i for i in range(n)}

        # 并查集
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        # 查找根节点
        for l, r in pairs:
            a, b = find(l), find(r)
            if a != b:
                parent[b] = a
        # 获取根节点对应的连通块集合
        dic = collections.defaultdict(list)
        for i in range(n):
            root = find(i)
            dic[root].append(i)
        # 对每个连通块中元素排序
        res = list(s)
        for k, v in dic.items():
            arr = [s[i] for i in v]
            arr.sort()
            for i in range(len(v)):
                res[v[i]] = arr[i]

        return "".join(res)


if __name__ == '__main__':
    s = "dcab"
    pairs = [[0, 3], [1, 2]]
    print(Solution().smallestStringWithSwaps(s, pairs))
